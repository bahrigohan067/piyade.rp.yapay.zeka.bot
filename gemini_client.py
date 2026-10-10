import aiohttp
import asyncio
from typing import List, Dict, Optional
import config
from knowledge_base import PIYADE_RP_SYSTEM_PROMPT

class GeminiClient:
    def __init__(self, api_key: str = None, model: str = None):
        self.api_key = api_key or config.GEMINI_API_KEY
        self.model = model or config.GEMINI_MODEL
        self.base_url = "https://generativelanguage.googleapis.com/v1beta/models"

    def has_api_key(self) -> bool:
        return bool(self.api_key and self.api_key.strip())

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
            # API anahtarı tanımlanmamışsa profesyonel yedek metin
            fallback_text = (
                f"Merhaba **{user_name}**,\n\n"
                "Destek talebiniz başarıyla kayıt altına alınmıştır. "
                "Yapay zeka asistanı şu anda bekleme modundadır.\n\n"
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

        endpoint = f"{self.base_url}/{self.model}:generateContent?key={self.api_key}"

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

        # Yeniden deneme mekanizması (3 deneme)
        for attempt in range(3):
            try:
                timeout = aiohttp.ClientTimeout(total=30)
                async with aiohttp.ClientSession(timeout=timeout) as session:
                    async with session.post(endpoint, json=payload) as resp:
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

                        elif resp.status in (429, 503, 500):
                            # Rate limit veya geçici sunucu hatası - bekle ve tekrar dene
                            await asyncio.sleep(2 * (attempt + 1))
                            continue
                        else:
                            error_text = await resp.text()
                            print(f"[Gemini API Hata]: HTTP {resp.status} - {error_text}")
                            break
            except asyncio.TimeoutError:
                await asyncio.sleep(1)
            except Exception as e:
                print(f"[Gemini API Exception]: {e}")
                break

        # Başarısız olursa kullanıcıya profesyonel devir mesajı ver
        return False, (
            f"Merhaba **{user_name}**,\n\n"
            "Sorunuzu değerlendirirken teknik bir aksaklık yaşandı. "
            "Destek talebiniz yetkili kadromuza iletilmiştir.\n\n"
            "🛡️ **Yetkililerimiz en kısa sürede sizinle ilgilenecektir.** "
            "Lütfen bekleyiniz, teşekkür ederiz."
        )
