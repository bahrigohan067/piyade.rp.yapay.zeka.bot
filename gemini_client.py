import aiohttp
import asyncio
from typing import List, Dict, Optional
import config
from knowledge_base import PIYADE_RP_SYSTEM_PROMPT
from security import (
    SECURITY_WARNING_REPLY,
    PROMPT_INJECTION_BARRIERS,
    is_prompt_injection,
    sanitize_user_input
)

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

        # ── 1. GÜVENLİK KONTROLÜ: PROMPT INJECTION / JAILBREAK DENETİMİ ──
        for msg in messages:
            if msg.get("role") == "user":
                raw_user_msg = msg.get("content", "")
                if is_prompt_injection(raw_user_msg):
                    print(f"[GÜVENLİK ENGELİ] Prompt Injection / Jailbreak tespit edildi! Kullanıcı: {user_name} -> {raw_user_msg}")
                    return True, SECURITY_WARNING_REPLY

        # ── 2. GÜVENLİ FORMATLAMA: KULLANICI GİRDİLERİNİ SİSTEM TALİMATLARINDAN AYRIŞTIR ──
        contents = []
        for msg in messages:
            role = "user" if msg.get("role") == "user" else "model"
            text = msg.get("content", "").strip()
            if text:
                if role == "user":
                    clean_text = sanitize_user_input(text)
                    formatted_text = f"<user_query author=\"{user_name}\">\n{clean_text}\n</user_query>"
                else:
                    formatted_text = text

                contents.append({
                    "role": role,
                    "parts": [{"text": formatted_text}]
                })

        if not contents:
            return False, "Soru içeriği boş iletildi. Lütfen sorunuzu detaylıca belirtiniz."

        # ── 3. SİSTEM PROMPTU VE ÇİFT KATMANLI KORUMA BARİYERLERİ ──
        system_text = (
            f"{PIYADE_RP_SYSTEM_PROMPT}\n\n"
            f"{PROMPT_INJECTION_BARRIERS}\n\n"
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

        # Model alternatifleri (en kararlı güncel modeller)
        models_to_try = []
        for m in [self.model, "gemini-2.0-flash", "gemini-1.5-flash"]:
            if m and m not in models_to_try:
                models_to_try.append(m)

        for current_model in models_to_try:
            # 1. Öncelik: Resmi X-Goog-Api-Key Başlığı
            configs = [
                (
                    f"{self.base_url}/{current_model}:generateContent",
                    {"x-goog-api-key": self.api_key, "Content-Type": "application/json"}
                ),
                (
                    f"{self.base_url}/{current_model}:generateContent?key={self.api_key}",
                    {"Content-Type": "application/json"}
                )
            ]

            for endpoint, hdrs in configs:
                try:
                    timeout = aiohttp.ClientTimeout(total=8, connect=3)
                    async with aiohttp.ClientSession(timeout=timeout) as session:
                        async with session.post(endpoint, json=payload, headers=hdrs) as resp:
                            if resp.status == 200:
                                data = await resp.json()
                                candidates = data.get("candidates", [])
                                if candidates:
                                    parts = candidates[0].get("content", {}).get("parts", [])
                                    if parts:
                                        reply = parts[0].get("text", "").strip()
                                        if reply:
                                            return True, reply

                                return False, ""

                            elif resp.status in (400, 401):
                                # Auth yöntemi uyuşmazlığı olabilir, diğer auth yöntemini dene
                                continue

                            elif resp.status == 404:
                                # Model ismi desteklenmiyor, bir sonraki modele geç
                                break

                except (asyncio.TimeoutError, asyncio.CancelledError):
                    break
                except Exception as e:
                    print(f"[Gemini Client] İstek hatası ({current_model}): {e}")
                    break

        return False, ""

