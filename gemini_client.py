import aiohttp
import asyncio
from typing import List, Dict, Optional
import config
from knowledge_base import PIYADE_RP_SYSTEM_PROMPT

class GeminiClient:
    def __init__(self, api_key: str = None, model: str = None):
        raw_key = api_key or config.GEMINI_API_KEY
        # Anahtarı tırnak ve boşluklardan tamamen arındır
        self.api_key = raw_key.strip().strip("'\"") if raw_key else ""
        self.model = (model or config.GEMINI_MODEL or "gemini-2.0-flash").strip().strip("'\"")
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models"

    def has_api_key(self) -> bool:
        return bool(self.api_key and len(self.api_key) > 10)

    async def generate_response(
        self,
        messages: List[Dict[str, str]],
        user_name: str = "Katılımcı",
        ticket_channel_name: str = "ticket"
    ) -> tuple[bool, str]:
        """
        Gemini API'sine istek atar ve yanıtı döndürür.
        Dönüş: (basarili_mi: bool, yanit_metni: str)
        """
        if not self.has_api_key():
            fallback_text = (
                f"Merhaba **{user_name}**,\n\n"
                "Destek talebiniz başarıyla kayıt altına alınmıştır.\n\n"
                "🛡️ **Yetkililerimiz en kısa sürede sizinle ilgilenecektir.** "
                "Lütfen bu süreçte talebinizle ilgili detayları veya kanıtlarınızı paylaşınız."
            )
            return False, fallback_text

        # Gemini v1beta chat formatına dönüştür
        contents = []
        for msg in messages:
            role = "user" if msg.get("role") == "user" else "model"
            text = msg.get("content", "").strip()
            if text:
                contents.append({
                    "role": role,
                    "parts": [{"text": text}]
                })

        if not contents:
            return False, "Soru içeriği boş iletildi. Lütfen sorunuzu detaylıca belirtiniz."

        # Context-rich sistem promptu
        system_text = (
            f"{PIYADE_RP_SYSTEM_PROMPT}\n\n"
            f"ŞU ANKİ DESTEK BİLETİ BİLGİLERİ:\n"
            f"- Kullanıcı Adı: {user_name}\n"
            f"- Bilet Kanalı: #{ticket_channel_name}\n"
            f"Kullanıcıya hitap ederken saygılı ve samimi ol. "
            f"Eğer sorun doğrudan çözülemiyorsa veya yetkili müdahalesi gerektiriyorsa "
            f"'Yetkililerimiz en kısa sürede sizinle ilgilenecektir' ifadesini eklemeyi unutma."
        )

        payload = {
            "system_instruction": {
                "parts": [{"text": system_text}]
            },
            "contents": contents,
            "generationConfig": {
                "temperature": 0.4,
                "topP": 0.95,
                "maxOutputTokens": 2048
            }
        }

        # Resmi Google Gemini başlıkları (x-goog-api-key)
        headers = {
            "x-goog-api-key": self.api_key,
            "Content-Type": "application/json"
        }

        # Model alternatifleri (varsayılan model desteklenmezse sırayla dener)
        candidate_models = [self.model, "gemini-2.0-flash", "gemini-1.5-flash"]
        # Tekrar edenleri temizle
        models_to_try = []
        for m in candidate_models:
            if m not in models_to_try:
                models_to_try.append(m)

        for current_model in models_to_try:
            endpoint = f"{self.base_url}/{current_model}:generateContent?key={self.api_key}"

            for attempt in range(2):
                try:
                    timeout = aiohttp.ClientTimeout(total=25)
                    async with aiohttp.ClientSession(timeout=timeout) as session:
                        async with session.post(endpoint, json=payload, headers=headers) as resp:
                            if resp.status == 200:
                                data = await resp.json()
                                candidates = data.get("candidates", [])
                                if candidates:
                                    parts = candidates[0].get("content", {}).get("parts", [])
                                    if parts:
                                        reply = parts[0].get("text", "").strip()
                                        if reply:
                                            return True, reply

                                return False, (
                                    "Yanıt üretilemedi. "
                                    "🛡️ **Yetkililerimiz en kısa sürede sizinle ilgilenecektir.**"
                                )

                            elif resp.status == 401:
                                error_text = await resp.text()
                                print(f"[Gemini API Hata]: HTTP 401 - Yetkilendirme Hatası! Lütfen GEMINI_API_KEY değerini kontrol edin.")
                                print(f"[Detay]: {error_text}")
                                # 401 anahtar hatasıdır, model değiştirmek çözmez
                                return False, (
                                    f"Merhaba **{user_name}**,\n\n"
                                    "Sorunuzu değerlendirirken teknik bir aksaklık yaşandı. "
                                    "Destek talebiniz yetkili kadromuza iletilmiştir.\n\n"
                                    "🛡️ **Yetkililerimiz en kısa sürede sizinle ilgilenecektir.** "
                                    "Lütfen bekleyiniz, teşekkür ederiz."
                                )

                            elif resp.status in (404, 400):
                                # Model bulunamadıysa bir sonraki modele geç
                                error_text = await resp.text()
                                print(f"[Gemini API]: {current_model} çalışmadı ({resp.status}), alternatif modele geçiliyor...")
                                break

                            elif resp.status in (429, 503, 500):
                                await asyncio.sleep(1.5 * (attempt + 1))
                                continue

                except asyncio.TimeoutError:
                    await asyncio.sleep(1)
                except Exception as e:
                    print(f"[Gemini API Exception]: {e}")
                    break

        return False, (
            f"Merhaba **{user_name}**,\n\n"
            "Sorunuzu değerlendirirken teknik bir aksaklık yaşandı. "
            "Destek talebiniz yetkili kadromuza iletilmiştir.\n\n"
            "🛡️ **Yetkililerimiz en kısa sürede sizinle ilgilenecektir.** "
            "Lütfen bekleyiniz, teşekkür ederiz."
        )
