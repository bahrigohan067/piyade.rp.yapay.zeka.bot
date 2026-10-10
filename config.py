import os

# Otomatik .env okuyucu (ekstra kütüphane gerektirmeden çalışır)
env_file = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(env_file):
    with open(env_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip("'\""))

# Bot Tokeni (Öncelik TOKEN_AL_BOT, alternatif olarak TOKEN veya DISCORD_TOKEN)
TOKEN = os.getenv("TOKEN_AL_BOT") or os.getenv("TOKEN") or os.getenv("DISCORD_TOKEN") or ""

# Google Gemini API Anahtarı
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "").strip()

# Gemini Modeli (En kararlı ve hızlı varsayılan model: gemini-2.0-flash)
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash").strip()

# Sunucu ve Rol Ayarları (Piyade RP Sunucusu)
GUILD_ID = int(os.getenv("GUILD_ID", "1529545898294509589"))
TICKET_YETKILI_ROL_ID = int(os.getenv("TICKET_YETKILI_ROL_ID", "1553333289798869032"))
KURUCU_ROL_ID = int(os.getenv("KURUCU_ROL_ID", "1529546007635824680"))

# Tasarım Renkleri (Açık Mavi Tema)
COLOR_LIGHT_BLUE = 0x38B6FF       # RGB: 56, 182, 255 (Açık Mavi)
COLOR_THINKING = 0x64B5F6         # Düşünme esnasındaki yumuşak açık mavi
COLOR_ALERT = 0x29B6F6            # Yetkili devri açık mavi tonu

# Ticket Ayarları
TICKET_CHANNEL_PREFIX = "ticket-"
TICKET_TOPIC_KEY = "acan_id:"
