import os
import json
import asyncio
from datetime import datetime, timezone
import discord
from discord.ext import commands
from discord import app_commands
import config
from gemini_client import GeminiClient

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
ANSWERED_FILE = os.path.join(DATA_DIR, "answered_tickets.json")

class TicketActionsView(discord.ui.View):
    """
    Yapay zeka yanıtının altına eklenen interaktif butonlar.
    """
    def __init__(self, ticket_owner_id: int = None, cog_ref = None):
        super().__init__(timeout=None)
        self.ticket_owner_id = ticket_owner_id
        self.cog_ref = cog_ref

    @discord.ui.button(
        label="Yetkili Çağır",
        style=discord.ButtonStyle.secondary,
        emoji="🛎️",
        custom_id="btn_ai_call_staff"
    )
    async def call_staff(self, interaction: discord.Interaction, button: discord.ui.Button):
        guild = interaction.guild
        staff_role = guild.get_role(config.TICKET_YETKILI_ROL_ID) if guild else None
        staff_mention = staff_role.mention if staff_role else "Yetkililer"

        embed = discord.Embed(
            title="🔔 Yetkili Bildirimi İletildi",
            description=(
                f"{interaction.user.mention} tarafından yetkili desteği talep edildi.\n\n"
                f"> **Görevli Kadro:** {staff_mention}\n"
                f"> Lütfen yetkililerimiz biletinize dönüş yapana kadar sabırla bekleyiniz."
            ),
            color=config.COLOR_LIGHT_BLUE
        )
        embed.set_footer(text="Piyade Roleplay Destek Ekibi")
        embed.timestamp = discord.utils.utcnow()

        await interaction.response.send_message(
            content=f"{staff_mention}" if staff_role else None,
            embed=embed
        )

    @discord.ui.button(
        label="Sorunum Çözüldü",
        style=discord.ButtonStyle.success,
        emoji="✅",
        custom_id="btn_ai_problem_solved"
    )
    async def problem_solved(self, interaction: discord.Interaction, button: discord.ui.Button):
        embed = discord.Embed(
            title="🌸 Yardımcı Olabildiğimize Sevindik!",
            description=(
                f"Harika bir haber {interaction.user.mention}! Sorununuzun çözülmesine çok sevindik. 🎉\n\n"
                f"Biletinizi kapatmak için yukarıdaki **'🔒 Kapat'** butonunu kullanabilir "
                f"veya yetkililerimizin biletinizi sonlandırmasını bekleyebilirsiniz.\n\n"
                f"*İyi ve keyifli roller dileriz!* ✨"
            ),
            color=config.COLOR_LIGHT_BLUE
        )
        embed.set_footer(text="Piyade RP | Los Angeles")
        embed.timestamp = discord.utils.utcnow()

        await interaction.response.send_message(embed=embed)

    @discord.ui.button(
        label="Başka Sorum Var",
        style=discord.ButtonStyle.primary,
        emoji="❓",
        custom_id="btn_ai_ask_again"
    )
    async def ask_again(self, interaction: discord.Interaction, button: discord.ui.Button):
        channel = interaction.channel
        if self.cog_ref and channel:
            self.cog_ref.unmark_answered(channel.id)

        await interaction.response.send_message(
            f"🤖 {interaction.user.mention}, yapay zeka tekrar dinlemeye alındı! Lütfen ek sorunuzu yazınız.",
            ephemeral=True
        )


class AITicketAssistant(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.gemini = GeminiClient()
        self.greeted_channels: set[int] = set()
        self.answered_channels: set[int] = set()
        self._load_cache()

    def _load_cache(self):
        """Kalıcı olarak cevaplanmış biletleri dosyadan yükler (Railway restart koruması)."""
        os.makedirs(DATA_DIR, exist_ok=True)
        if os.path.exists(ANSWERED_FILE):
            try:
                with open(ANSWERED_FILE, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.answered_channels = set(data.get("answered", []))
                    self.greeted_channels = set(data.get("greeted", []))
            except Exception:
                pass

    def _save_cache(self):
        """Cevaplanan bilet durumunu diske yazar."""
        os.makedirs(DATA_DIR, exist_ok=True)
        try:
            with open(ANSWERED_FILE, "w", encoding="utf-8") as f:
                json.dump({
                    "answered": list(self.answered_channels),
                    "greeted": list(self.greeted_channels)
                }, f)
        except Exception:
            pass

    def unmark_answered(self, channel_id: int):
        """Kullanıcı butonla tekrar soru sormak isterse kilidi açar."""
        self.answered_channels.discard(channel_id)
        self._save_cache()

    def is_ticket_channel(self, channel: discord.abc.GuildChannel) -> bool:
        """Kanalın Piyade RP bilet kanalı olup olmadığını kontrol eder."""
        if not isinstance(channel, discord.TextChannel):
            return False
        
        # 1. Kural: Kanal adı 'ticket-' ile başlar (Örn: ticket-ahmet)
        if channel.name.lower().startswith(config.TICKET_CHANNEL_PREFIX):
            return True
        
        # 2. Kural: Kanal topic kısmında acan_id etiketi yer alır
        if channel.topic and config.TICKET_TOPIC_KEY in channel.topic:
            return True
            
        return False

    def get_ticket_owner_id(self, channel: discord.TextChannel) -> int | None:
        """Bileti açan kullanıcının Discord ID'sini tespit eder."""
        if channel.topic and config.TICKET_TOPIC_KEY in channel.topic:
            try:
                part = channel.topic.split(config.TICKET_TOPIC_KEY)[1].strip()
                digits = "".join([c for c in part if c.isdigit()])
                if digits:
                    return int(digits)
            except Exception:
                pass

        for target, overwrite in channel.overwrites.items():
            if isinstance(target, discord.Member) and not target.bot:
                if overwrite.view_channel is True and overwrite.send_messages is True:
                    return target.id

        return None

    async def has_already_answered(self, channel: discord.TextChannel) -> bool:
        """
        Bu bilet kanalına yapay zekanın daha önce 1 kez cevap verip vermediğini kesin denetler.
        """
        # 1. Önbellekte var mı?
        if channel.id in self.answered_channels:
            return True

        # 2. Kanalın mesaj geçmişinde botun nihai çözüm mesajı var mı?
        try:
            async for msg in channel.history(limit=30):
                if msg.author == self.bot.user and msg.embeds:
                    for emb in msg.embeds:
                        if emb.title and ("💎 Piyade AI | Çözüm & Bilgilendirme" in emb.title or "⚠️ Destek Servisi Bilgilendirmesi" in emb.title):
                            self.answered_channels.add(channel.id)
                            self._save_cache()
                            return True
        except Exception:
            pass

        return False

    async def send_welcome_greeting(self, channel: discord.TextChannel, owner: discord.Member | None = None):
        """Bilet açıldığında kullanıcıyı etiketleyip şık bir hoş geldin sorusu sorar (Sadece 1 kez)."""
        if channel.id in self.greeted_channels:
            return

        try:
            async for msg in channel.history(limit=10):
                if msg.author == self.bot.user and "Size nasıl yardımcı olabiliriz?" in (msg.content or (msg.embeds[0].description if msg.embeds else "")):
                    self.greeted_channels.add(channel.id)
                    return
        except Exception:
            pass

        owner_id = owner.id if owner else self.get_ticket_owner_id(channel)
        owner_member = channel.guild.get_member(owner_id) if owner_id else owner

        mention_str = owner_member.mention if owner_member else "Değerli Üyemiz"

        embed = discord.Embed(
            title="💎 Piyade Roleplay | Yapay Zeka Destek Hattı",
            description=(
                f"Merhaba {mention_str}, **Piyade Roleplay Destek Merkezi**'ne hoş geldiniz! 🌸\n\n"
                f"Ben **Piyade AI Destek Asistanı** 🤖. Sunucumuzun kuralları, sistemleri, "
                f"kayıt adımları ve tüm mekanikleri hakkında sizlere rehberlik etmek için buradayım.\n\n"
                f"### 💬 Size nasıl yardımcı olabiliriz?\n"
                f"Lütfen yaşamakta olduğunuz sorunu, merak ettiğiniz konuyu veya talebinizi "
                f"aşağıya detaylı bir şekilde yazınız.\n\n"
                f"──────────────────────────────────────────\n"
                f"💡 *Sorunuzu ilettiğinizde sunucu kayıtları taranarak anında çözüm üretilecektir.*"
            ),
            color=config.COLOR_LIGHT_BLUE
        )

        if channel.guild.icon:
            embed.set_thumbnail(url=channel.guild.icon.url)
        embed.set_footer(text="Piyade RP • Yapay Zeka Destek Sistemi • Sizin İçin Buradayız")
        embed.timestamp = discord.utils.utcnow()

        try:
            await channel.send(content=f"{mention_str}", embed=embed)
            self.greeted_channels.add(channel.id)
            self._save_cache()
        except Exception as e:
            print(f"[AITicketAssistant] Karşılama mesajı gönderilemedi: {e}")

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel: discord.abc.GuildChannel):
        """Ana bot tarafından yeni bir ticket kanalı oluşturulduğunda tetiklenir."""
        if not self.is_ticket_channel(channel):
            return

        await asyncio.sleep(1.5)
        if isinstance(channel, discord.TextChannel):
            await self.send_welcome_greeting(channel)

    def is_complaint_or_report(self, text: str) -> bool:
        """
        Kullanıcının iletisinin bir üye şikayeti, rol hatası, kural ihlali veya yanlış işlem
        bildirimi olup olmadığını tespit eder.
        """
        t = text.lower()

        # Doğrudan şikayet ve ihlal kalıpları
        complaint_keywords = [
            "şikayet", "sikayet", "şikayetçi", "sikayetci", "şikayetim",
            "rapor", "report", "troll", "trolledi", "trollüyor", "trolluyor",
            "rdm", "vdm", "frp", "cl attı", "cl atti", "combat log",
            "fear rp", "cop bait", "cop trigger", "nlr", "gooa", "trash talk",
            "rol hatası", "rol hatasi", "yanlış işlem", "yanlis islem", "haksız işlem", "haksiz islem",
            "kural ihlali", "ihlal etti", "ihlal var",
            "öldürdü", "oldurdu", "öldürdüler", "oldurduler", "vurdu", "vurdular", "sıktı", "sikti",
            "küfür etti", "kufur etti", "hakaret etti", "taciz etti", "dolandırdı", "dolandirdi",
            "kanıtım var", "kanitim var", "klip var", "klibim var", "video var", "videom var", "ss var", "ss aldım",
            "banlansın", "ban atılsın", "cezalandırılsın", "ceza verilsin", "uyarı verilsin",
            "haksız yere", "haksiz yere", "sebepsiz yere"
        ]

        definition_queries = ["nedir", "ne demek", "anlamı ne", "nasıl yapılır", "açıklar mısın", "nelerdir"]
        is_asking_definition = any(dq in t for dq in definition_queries)

        for kw in complaint_keywords:
            if kw in t:
                if "şikayet" in t or "sikayet" in t or "rapor" in t or "report" in t:
                    return True
                if not is_asking_definition:
                    return True

        return False

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        """Ticket kanallarına gelen mesajları dinler ve yapay zeka ile SADECE 1 KEZ yanıtlar."""
        if message.author.bot or not message.guild:
            return

        channel = message.channel
        if not self.is_ticket_channel(channel):
            return

        # ── KRİTİK KONTROL: Bot bu bilette zaten 1 kez cevap verdi mi? ──
        # Eğer daha önce cevap verdiyse artık kanaldaki sohbeti yetkililere ve kullanıcıya bırakır, ASLA ARAYA GİRMEZ!
        if await self.has_already_answered(channel):
            return

        # Kanal henüz selamlanmadıysa ilk mesajda selamla
        if channel.id not in self.greeted_channels:
            bot_msg_exists = False
            async for m in channel.history(limit=5):
                if m.author == self.bot.user:
                    bot_msg_exists = True
                    break
            if not bot_msg_exists:
                await self.send_welcome_greeting(channel, message.author)

        prompt_text = message.content.strip()
        if not prompt_text:
            return

        owner_id = self.get_ticket_owner_id(channel)

        # ── ŞİKAYET / ROL HATASI / KURAL İHLALİ KONTROLÜ ──
        # Eğer kullanıcı bir üyeyi şikayet ettiyse veya ihlal bildirdiyse:
        # Bot buna cevap vermez (Gemini çağrılmaz, düşünme mesajı atılmaz).
        # Doğrudan yetkiliye yönlendirir ve kanıt talep eder!
        if self.is_complaint_or_report(prompt_text):
            staff_role = message.guild.get_role(config.TICKET_YETKILI_ROL_ID)
            staff_mention = staff_role.mention if staff_role else "Yetkililer"

            complaint_embed = discord.Embed(
                title="🛡️ Piyade Roleplay | Yetkili İncelemesine Yönlendirildi",
                description=(
                    f"Merhaba {message.author.mention},\n\n"
                    "İletmiş olduğunuz talep bir **üye şikayeti / rol hatası / kural ihlali** kapsamındadır.\n\n"
                    "⚖️ **Bu işlem doğrudan yetkili ekibimiz tarafından incelenmektedir.**\n"
                    "Yapay zeka şikayet değerlendirmesi ve ceza işlemlerine dahil olamaz.\n\n"
                    "📌 **Lütfen yetkili ekibimiz kanala gelene kadar:**\n"
                    "• Olayla ilgili **video kaydınızı (klip) veya ekran görüntüsü (SS)** kanıtlarınızı bu kanala yükleyiniz.\n"
                    "• Şikayetçi olduğunuz kişinin **Roblox Adı ve Discord etiketini/ID'sini** yazınız.\n"
                    "• Yaşanan olayı kısa ve net bir şekilde özetleyiniz.\n\n"
                    "──────────────────────────────────────────\n"
                    "🔔 **Yetkili kadromuza bildirim iletildi.** En kısa sürede biletinizle ilgileneceklerdir."
                ),
                color=config.COLOR_LIGHT_BLUE
            )
            if message.guild.icon:
                complaint_embed.set_thumbnail(url=message.guild.icon.url)
            complaint_embed.set_footer(text="Piyade Roleplay Şikayet & Disiplin Yönetimi")
            complaint_embed.timestamp = discord.utils.utcnow()

            await channel.send(
                content=f"{staff_mention} | {message.author.mention}",
                embed=complaint_embed,
                view=TicketActionsView(ticket_owner_id=owner_id, cog_ref=self)
            )

            # Bu bilet için işlem tamamlandı, yapay zeka artık kanaldan çekilir
            self.answered_channels.add(channel.id)
            self._save_cache()
            return

        # ── 1. Adım: Bilgi Sorusuysa Açık Mavi "Düşünüyor..." Mesajını Gönder ──
        thinking_embed = discord.Embed(
            title="🤖 Piyade AI Destek Asistanı",
            description=(
                "🌀 **Düşünüyor...**\n\n"
                "> *Sorunuz ve sunucumuzun sistem kayıtları inceleniyor, lütfen bekleyiniz...*"
            ),
            color=config.COLOR_THINKING
        )
        thinking_embed.set_footer(text="Piyade RP Bilgi Bankası Taranıyor...")
        thinking_embed.timestamp = discord.utils.utcnow()

        try:
            thinking_msg = await channel.send(embed=thinking_embed)
        except Exception as e:
            print(f"[AITicketAssistant] Düşünme mesajı gönderilemedi: {e}")
            return

        # ── 2. Adım: Cevap Üretilirken Kanalı "Cevaplandı" Olarak Kilitle ──
        self.answered_channels.add(channel.id)
        self._save_cache()

        # Discord 'yazıyor...' animasyonunu başlat
        try:
            async with channel.typing():
                # Sohbet Geçmişi
                history = []
                async for past_msg in channel.history(limit=8, before=thinking_msg):
                    if not past_msg.content:
                        continue
                    if past_msg.author == self.bot.user:
                        history.append({"role": "model", "content": past_msg.content})
                    elif not past_msg.author.bot:
                        history.append({"role": "user", "content": past_msg.content})

                history.reverse()
                history.append({"role": "user", "content": prompt_text})

                # Gemini AI Çağrısı
                user_display_name = message.author.display_name
                success, ai_reply = await self.gemini.generate_response(
                    messages=history,
                    user_name=user_display_name,
                    ticket_channel_name=channel.name
                )

                # Yetkili Devri Kontrolü
                needs_staff = (
                    not success or
                    "yetkili" in ai_reply.lower() and ("ilgilen" in ai_reply.lower() or "onay" in ai_reply.lower() or "müdahale" in ai_reply.lower())
                )

                clean_reply = ai_reply
                if len(clean_reply) > 3900:
                    clean_reply = clean_reply[:3850] + "\n\n*(Cevabın devamı için lütfen detay sorunuz...)*"

                response_embed = discord.Embed(
                    title="💎 Piyade AI | Çözüm & Bilgilendirme",
                    description=clean_reply,
                    color=config.COLOR_LIGHT_BLUE
                )

                if message.guild.icon:
                    response_embed.set_thumbnail(url=message.guild.icon.url)

                if needs_staff:
                    response_embed.add_field(
                        name="🛡️ Yetkili Ekibi Bilgilendirmesi",
                        value=(
                            "Yetkililerimiz en kısa sürede sizinle ilgilenecektir.\n"
                            "Gerekirse aşağıdaki **'Yetkili Çağır'** butonuna basarak yetkili ekibine doğrudan bildirim gönderebilirsiniz."
                        ),
                        inline=False
                    )

                response_embed.set_footer(text=f"Soruyu Soran: {user_display_name} • Piyade Roleplay Destek")
                response_embed.timestamp = discord.utils.utcnow()

                # ── 3. Adım: "Düşünüyor..." Mesajını Güncelle ve Butonları Ekle ──
                view = TicketActionsView(ticket_owner_id=owner_id, cog_ref=self)
                await thinking_msg.edit(embed=response_embed, view=view)

        except Exception as e:
            print(f"[AITicketAssistant] Mesaj yanıtlama hatası: {e}")
            try:
                error_embed = discord.Embed(
                    title="⚠️ Destek Servisi Bilgilendirmesi",
                    description=(
                        "Sorunuz işlenirken beklenmeyen bir hata meydana geldi.\n\n"
                        "🛡️ **Yetkililerimiz en kısa sürede sizinle ilgilenecektir.** "
                        "Lütfen endişelenmeyiniz, talebiniz kayıtlarımızdadır."
                    ),
                    color=config.COLOR_LIGHT_BLUE
                )
                await thinking_msg.edit(embed=error_embed, view=TicketActionsView(owner_id, cog_ref=self))
            except Exception:
                pass

    @app_commands.command(
        name="ai_selam",
        description="Mevcut bilet kanalına yapay zeka karşılama mesajını gönderir."
    )
    async def ai_selam(self, interaction: discord.Interaction):
        if not self.is_ticket_channel(interaction.channel):
            return await interaction.response.send_message(
                "❌ Bu komut yalnızca bilet (`ticket-*`) kanallarında kullanılabilir.",
                ephemeral=True
            )

        await interaction.response.defer(ephemeral=True)
        await self.send_welcome_greeting(interaction.channel, interaction.user)
        await interaction.followup.send("✅ Yapay zeka karşılama mesajı gönderildi.", ephemeral=True)


async def setup(bot: commands.Bot):
    cog = AITicketAssistant(bot)
    await bot.add_cog(cog)
    bot.add_view(TicketActionsView(cog_ref=cog))
