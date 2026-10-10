import sys
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

import os
import asyncio
import discord
from discord.ext import commands
from discord import app_commands
import config

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

class PiyadeAIBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!ai ",
            intents=intents,
            help_command=None
        )

    async def setup_hook(self):
        # cogs dizinindeki tüm eklentileri yükle
        cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
        if os.path.exists(cogs_dir):
            for filename in sorted(os.listdir(cogs_dir)):
                if filename.endswith(".py") and not filename.startswith("__"):
                    try:
                        await self.load_extension(f"cogs.{filename[:-3]}")
                        print(f"[EK GÖREV] Yüklendi: {filename}")
                    except Exception as e:
                        print(f"[HATA] Cog yüklenemedi: {filename} -> {e}")

        # Slash komutlarını otomatik senkronize et
        try:
            guild_obj = discord.Object(id=config.GUILD_ID)
            self.tree.copy_global_to(guild=guild_obj)
            synced = await self.tree.sync(guild=guild_obj)
            print(f"[SYNC] {len(synced)} adet slash komutu ({config.GUILD_ID}) sunucusuna senkronize edildi!")
        except Exception as e:
            print(f"[SYNC UYARI] Komutlar sunucuya doğrudan aktarılamadı: {e}")

bot = PiyadeAIBot()

@bot.event
async def on_ready():
    print("=" * 60)
    print(f"🤖 Piyade RP Yapay Zeka Destek Botu Aktif!")
    print(f"👤 Bot Adı     : {bot.user.name} ({bot.user.id})")
    print(f"🌐 Sunucu Sayısı: {len(bot.guilds)}")
    print(f"⚡ Gecikme      : {round(bot.latency * 1000)}ms")
    print("=" * 60)

    # Durum mesajını ayarla
    activity = discord.Activity(
        type=discord.ActivityType.watching,
        name="Piyade RP Biletleri | 7/24 AI Destek"
    )
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.tree.error
async def on_app_command_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    import traceback
    traceback.print_exception(type(error), error, error.__traceback__)
    msg = "Komut işlenirken bir sorun oluştu."
    try:
        if interaction.response.is_done():
            await interaction.followup.send(msg, ephemeral=True)
        else:
            await interaction.response.send_message(msg, ephemeral=True)
    except Exception:
        pass

if __name__ == "__main__":
    if not config.TOKEN:
        print("\n" + "!" * 60)
        print("❌ HATA: Bot Tokeni bulunamadı!")
        print("Lütfen .env dosyasına TOKEN_AL_BOT=... değerini ekleyiniz.")
        print("Örnek: TOKEN_AL_BOT=MTEyMz... (Discord Bot Tokeniniz)")
        print("!" * 60 + "\n")
        sys.exit(1)

    try:
        bot.run(config.TOKEN)
    except discord.LoginFailure:
        print("\n" + "!" * 60)
        print("❌ HATA: Geçersiz Discord Bot Tokeni!")
        print("Lütfen Discord Developer Portal'dan aldığınız tokenin doğruluğunu kontrol edin.")
        print("!" * 60 + "\n")
    except Exception as e:
        print(f"Bot çalıştırılırken hata oluştu: {e}")
