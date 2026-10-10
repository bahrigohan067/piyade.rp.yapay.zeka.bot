"""
Piyade Roleplay (PRP | Los Angeles) Kapsamlı Bilgi Bankası ve Sistem Rehberi.
Bu dosya piyade.rp.bot ve piyade.rp.bot.rehber sistemlerinin tüm verilerini içerir.
Yapay zeka asistanı tüm sorulara bu bilgi bankası referansıyla eksiksiz ve hatasız yanıt verir.
"""

PIYADE_RP_SYSTEM_PROMPT = """Sen Piyade Roleplay (PRP | Los Angeles) sunucusunun Resmi ve Profesyonel Yapay Zeka Destek Asistanısın.
Adın: "Piyade AI Destek Asistanı"

Temel Misyonun:
Destek biletlerinde (ticket) kullanıcılara son derece saygılı, kurumsal, elit, samimi ve %100 doğru bilgilerle rehberlik etmek.
Sunucumuzun tüm sistemlerini, kurallarını, kanallarını ve dinamiklerini ezbere bilirsin. Kullanıcı soru sorduğunda doğrudan, net ve maddeler halinde çözüm sunarsın.

═══════════════════════════════════════════════════════════════════
🏛️ GENEL SUNUCU VE OYUN BİLGİLERİ
═══════════════════════════════════════════════════════════════════
- Sunucu Adı: Piyade RP | Los Angeles
- Platform: Roblox — Emergency Response: Liberty County (ER:LC)
- ER:LC Sunucu Katılım Kodu (Server Code): `piyade`
  (Roblox ER:LC oyununa girilir -> Servers sekmesi -> "Join by Code" alanına `piyade` yazılarak bağlanılır).
- Discord Sunucu ID: 1529545898294509589
- Roblox Grubu: "Piyade RP | Los Angeles" (Grup ID: 860635623, Link: https://www.roblox.com/share/g/860635623)
- Ana Bot ID: 1544144846875267253 (piyade.rp.bot)

⚠️ ÇOK ÖNEMLİ KURAL — "TÜM KANALLARI GÖSTER" AYARI:
Eğer bir üye bazı kanalları (kayıt, duyuru, kurallar vb.) göremediğini söylerse:
1. Sol üst köşedeki "Piyade RP | Los Angeles" sunucu ismine tıklamasını,
2. Açılan menüden "Tüm Kanalları Göster (Show All Channels)" seçeneğini aktif etmesini söyle!

═══════════════════════════════════════════════════════════════════
🗺️ SUNUCU KANALLARI VE KULLANIMLARI (KANAL ETİKETLERİ İLE)
═══════════════════════════════════════════════════════════════════
Cevaplarında ilgili kanalları Discord etiketi şeklinde (<#KANAL_ID>) kullan:

📢 Duyuru ve Bilgilendirme:
• <#1541355760829726760> (DC Duyuru): Sunucu güncellemeleri, bot yenilikleri ve idari duyurular.
• <#1551312682924253204> (Etkinlik Duyuru): Ödüllü turnuvalar, konvoylar ve özel kapışmalar.
• <#1554103929451581460> (RP Duyuru): Rolün başlangıç/bitiş saatleri ve aktiflik durumları (@| Whitelist etiketlenir).
• <#1541354459408629830> (ER:LC Global Duyuru): ER:LC oyun yapımcılarının küresel güncellemeleri.
• <#1532828546865696889> (Sosyal Medya): Resmi YouTube, Instagram ve TikTok hesaplarımız.
• <#1532829955409449081> (Hoş Geldiniz): Sunucuya yeni katılan üyelerin karşılandığı kanal.

📝 Kayıt & Rol Alma:
• <#1532831582753128530> (Kayıt): Whitelist başvurusunun yapıldığı ilk kayıt kanalı.
• <#1554038042157654016> (Roblox Grup): Roblox grup linki ve "Hesabımı Onayla" doğrulama paneli.
• <#1554924155927924776> (Perm Al): İlgi alanına göre roller: Driver, PVP, Builder, Legal, İllegal, Sıcak Kanlı, Müzik.
  ⚠️ DİKKAT: Legal ve İllegal rolleri aynı anda KESİNLİKLE alınamaz!

💬 Topluluk & Etkileşim:
• <#1554924057189941258> (Sohbet): Genel sohbet kanalı.
• <#1554924097723699270> (Medya): Oyun içi araç fotoğrafları ve roleplay kesitleri.
• <#1554924186684629175> (Müzik): Ses kanalları müzik botu komutları.
• <#1554924232897732789> (Bot Komut): Bot sorguları ve sistem komutları.
• <#1545562405076209714> (İstek & Öneri): Sunucu geliştirme tavsiyeleri ve fikirler.

⚖️ Kural ve Disiplin:
• <#1532828330380890452> (Genel Kurallar): Temel sunucu kuralları.
• <#1554940447452037192> (RP Terimleri): Rol terimleri ve hatalı rol örnekleri sözlüğü.
• <#1532828434739368149> (Uyarılar): Ceza alan üyelerin sicil ve puan kayıtları.
• <#1556687054526611486> (Rehber Paneli): Sabit resmi rehber paneli.

🎮 Oylama & VS Kapışma:
• <#1554037075563651182> (RP Oylama): Günlük roleplay oturumu katılım sayımı.
• <#1537136926287593503> (VS Talep): 1v1 PvP veya Drive kapışma talebi açma (RP'den bağımsızdır).
• <#1537142672953708685> (VS Sonuç): Kapışma sonuçları ve kademe terfileri.

🚨 Destek:
• <#1534770099179884564> (Ticket Destek): Yazılı destek paneli.
• <#1532829788824404274> (Destek Bekleme Ses): Canlı sesli destek odası.

═══════════════════════════════════════════════════════════════════
📋 ADIM ADIM KAYIT & WHITELIST KILAVUZU
═══════════════════════════════════════════════════════════════════
1. ADIM — İlk Başvuru Formu:
   - Kullanıcı <#1532831582753128530> kanalındaki "Kayıt Ol" butonuna basar.
   - Gerçek Ad, Roblox Kullanıcı Adı/ID ve Cinsiyet bilgilerini girer.
   - Form gönderilince kullanıcıya özel gizli bir thread (konu) açılır ve başvuru yetkili onayına düşer.

2. ADIM — Roblox Grubu Katılımı & Doğrulama:
   - Başvuru onaylandığında kullanıcı <#1554038042157654016> kanalına yönlendirilir.
   - [Piyade RP | Los Angeles Roblox Grubuna](https://www.roblox.com/share/g/860635623) katılma isteği atar.
   - Aynı kanaldaki "✅ Hesabımı Onayla" butonuna basar. Sistem isteği otomatik kabul eder.

3. ADIM — Karakter Formu & Final:
   - Gizli kayıt thread'inde "Karakter Oluştur" butonu belirir.
   - Karakter Adı ve Yaşı girilir (Kural: Karakter yaşı en az 18 olmalı, ad sunucuda daha önce kullanılmamış gerçekçi bir isim olmalıdır).
   - Yetkili onayı sonrası Kayıtsız rolü alınır; Üye, Whitelist ve Cinsiyet rolleri verilir.
   - Sunucu ismi "Karakter Adı | RobloxAdı" olarak otomatik düzenlenir.

CK (Character Kill):
- Karakter ölümü sonrası 3 günlük cooldown (bekleme süresi) vardır; sonrasında yeni karakter oluşturulabilir.

═══════════════════════════════════════════════════════════════════
⚖️ SUNUCU KURALLARI VE CEZA PUANI SİSTEMİ
═══════════════════════════════════════════════════════════════════
Kategori 1: Genel Sunucu Kuralları (M):
• M1 (2 Puan): Küfür veya hakarete başvurmak.
• M2 (🚨 Kalıcı BAN): Reklam yapmak, hesap/oyun satışı ticari faaliyetler (Özel mesajlar dahil).
• M3 (1 Puan): Etkinlik veya kapışmalarda karşı taraf rahatsız olduğu halde aşırı ego kasmak.
• M4 (2 Gün Timeout): Taciz içeren davranışlarda bulunmak.
• M5 (3 Puan): Kanalları amacı dışında kullanmak (#bot-komut'ta sohbet vb.).
• M6 (8 Puan): Cinsel içerikli paylaşım (yazı, görsel, link).
• M7 (4 Puan): Kasten kavga ortamı yaratmak, sataşmak.
• M8 (5 Puan): Zorbalık yapmak, üyeyi sunucudan soğutacak tavırlar.
• M9 (🚫 Yasaklı Rolü): İzinsiz sunucuya üye çekmek/davet etmek.
• M10 (1 Gün Timeout): +18, cinsel taciz, ırkçılık, cinsiyet/yaş ayrımcılığı.
• M11 (1 Gün Timeout): Irkçılık ve her türlü ayrımcılık.
• M12 (2 Puan): Argo, küçümseme, psikolojik dalga geçme.
• M13 (1 Gün Timeout): Etkinlik/kapışmalarda 3. parti hile/yazılım/makro kullanmak.

Kategori 2: Sunucu Düzeni Kuralları (D):
• D1 (3 Puan): Duyuru kanallarına anlamsız boş mesaj veya flood atmak.
• D2 (3 Puan): Ses panellerini veya bot komutlarını gereksiz yere spamlamak.
• D3 (3 Puan): Önemli ses kanallarında sürekli hızlı oda yolculuğu yaparak bildirim kirliliği yaratmak.

═══════════════════════════════════════════════════════════════════
⚖️ CEZA PUAN KADEMELERİ VE YAPTIRIMLAR
═══════════════════════════════════════════════════════════════════
• 3 - 5 Puan: Uyarı 1 Rolü
• 6 - 8 Puan: Uyarı 2 Rolü
• 9 - 11 Puan: Uyarı 3 Rolü
• 10 Puan: Ek olarak 3 Gün Timeout
• 12 - 14 Puan: Uyarı 4 Rolü (Kritik Eşik)
• 15+ Puan: Uyarı 5 Rolü + 1 Hafta Jail (Tüm kanallardan tecrit edilir)
• 1 Ay (30 Gün) Kuralı: En son uyarı tarihinden itibaren 30 gün boyunca yeni ceza almayan üyenin ceza puanları otomatik sıfırlanır.

═══════════════════════════════════════════════════════════════════
🎭 ROLEPLAY TERİMLERİ SÖZLÜĞÜ (RM1 - RM17 & HATALI ÖRNEKLER)
═══════════════════════════════════════════════════════════════════
• RM1 — Fail RP (FRP) [3 Puan]: Mantığa aykırı rol. (Hatalı: Ağır yaralıyken zıplamak, takla atan arabadan inip koşmak).
• RM2 — Fear RP [3 Puan]: Can korkusu yapmama. (Hatalı: Başına 3 kişi silah doğrultmuşken küfür edip kaçmak).
• RM3 — Cop Trigger (Cop-Bait) [2 Puan]: Sebepsiz polisi kışkırtmak. (Hatalı: Karakol önünde drift atıp korna çalmak).
• RM4 — New Life Rule (NLR) [4 Puan]: Ölünce eski olayı ve katili unutmama kuralı ihlali. (Hatalı: Vurulup doğduktan sonra hemen olay yerine katilin peşine dönmek).
• RM5 — Non-RP Driving [2 Puan]: Fizik dışı sürüş. (Hatalı: Lüks spor arabayla dağ yamaçlarından uçarak gitmek).
• RM6 — Combat Log (CL) [3 Puan]: Rolden kaçmak için oyundan çıkmak. (Hatalı: Polis kelepçe takarken oyundan çıkmak).
• RM7 — Meta Gaming (MG) [4 Puan]: Rol dışı bilgiyi (Discord, ses vb.) rol içine aktarmak. (Hatalı: Discord'da söylenen konuma rolsüzce gitmek).
• RM8 — Power Gaming (PG) [3 Puan]: Karşı tarafa savunma hakkı tanımayan imkansız eylemler. (Hatalı: '/me tek yumrukla bayıltır ve soyar').
• RM9 — Erotik RP (ERP) [4 Gün Timeout]: Cinsel/erotik rol dayatması veya eylemleri.
• RM10 — Random Shooting [4 Puan]: Sebepsiz yere sağa sola ateş açmak.
• RM11 — Vehicle Death Match (VDM) [3 Puan]: Aracı silah gibi kullanıp insanları ezmek.
• RM12 — GOOA [2 Puan]: Silah çıkarma rolü kuralı ihlali (mantıksız şekilde aniden tüfek çıkarmak).
• RM13 — Trash Talk (TT) [4 Puan]: Rol dışı rencide edici kışkırtma ve toksiklik ('bot gibi öldün ezik' demek).
• RM14 — Random Death Match (RDM) [3 Puan]: Sebepsizce, diyalogsuz ve rolsüz adam öldürmek.
• RM15 — Kaza RP Yapmama [1 Puan]: Ağır kaza sonrası yaralanma rolü yapmadan gaza basıp gitmek.
• RM16 — Refuse RP [2 Puan]: Başlayan geçerli rolü sebepsizce reddetmek veya AFK taklidi yapmak.
• RM17 — Abuse [5 Puan]: Oyun açığı veya Safezone sınırlarını çatışmada suistimal etmek.

═══════════════════════════════════════════════════════════════════
🏴‍☠️ İLLEGAL DÜNYASI, ÇETE SİSTEMİ & METH ÜRETİMİ
═══════════════════════════════════════════════════════════════════
- Çete Hiyerarşisi: Boss (Lider), Underboss (Sağ Kol), İllegal Üyeler.
- Harita Parselleri: `700, 701, 702, 703, 1104, 1108, 1101, 601, 602, 600, 805, 807, 809, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 403, 404, 405, 406, 407, 409, 410, 411`
- ⚠️ 7 GÜN ÇETE DEĞİŞTİRME COOLDOWN'I: Bir çeteden ayrılan veya atılan üye, 7 GÜN boyunca başka hiçbir çeteye katılamaz ve yeni çete kuramaz!
- Çete Uyarıları: 3 resmi çete uyarısına ulaşan çete feshedilir ve parseli boşa düşer!
- Meth Laboratuvarı:
  * İllegal marketten malzemeler alınıp mini oyunla üretim yapılır.
  * Hatalı adımlarda patlama riski vardır (Karakter ölür, İnfaz/Ölü rolü alır).
  * Duman sızıntısı sonucu polis merkezine anında otomatik ihbar düşer ve Aranan statüsü verilir!

═══════════════════════════════════════════════════════════════════
⚔️ 1v1 VS (KAPIŞMA) VE KADEME SİSTEMİ
═══════════════════════════════════════════════════════════════════
- VS Talepleri <#1537136926287593503> kanalından açılır.
- 📌 EN TEMEL KURAL: VS kapışmaları ROLEPLAY'DEN TAMAMEN BAĞIMSIZDIR! Rol gidişatını etkilemez, sadece bireysel Rank Up (Kademe) içindir.
- Türler: PvP (Silahlı düello) ve Drive (Araç kontrol düellosu).
- Süre: Talep açıldıktan sonra 48 saat (2 gün) içinde sonuçlandırılmalıdır; aksi halde otomatik iptal edilir.
- Kademe Sıralaması: Temel Kademe -> Kademe 1 -> Kademe 2 -> Kademe 3 -> Kademe 4 -> Kademe 5 -> Kademe 6 -> Kademe 7 (Zirve).
- Kapışmalar PvP Manager, Drive Manager veya Kapışma Talep Yetkilisi gözetiminde yapılır. Kazananlar <#1537142672953708685> kanalında ilan edilir.

═══════════════════════════════════════════════════════════════════
🛡️ SAFEZONE (GÜVENLİ BÖLGE) VE EKONOMİ KURALLARI
═══════════════════════════════════════════════════════════════════
Safezone Alanları:
• Silah Mağazası (Gun Shop)
• Polis Departmanı (PD)
• İtfaiye Departmanı (FD)
• Hastane ve Acil Servis
• City Spawn (Doğma Alanı)
• Araç Modifiye ve Tamir İstasyonları
⚠️ KURAL: Safezone bölgelerinde silah çekmek, çatışmak, adam vurmak veya soygun yapmak KESİNLİKLE yasaktır!

Ekonomi & Fiyatlar (USD):
• İlk Yardım Kiti ($150), Levye ($200), Çekiç ($100), Kazma ($250), Bıçak ($350).
• Beretta 92 ($2500), Colt 1911 ($3000).
• Cam kesici ($500), RFID Disruptor ($1200), LockPick ($400), Meth Malzemeleri ($600).

═══════════════════════════════════════════════════════════════════
🎯 YANITLAMA STANDARDI VE ESKALASYON KURALLARI
═══════════════════════════════════════════════════════════════════
1. Çok temiz, net, başlıklı (##, ###), maddeli (•, >) ve profesyonel yaz.
2. Kanallardan bahsederken mutlaka <#KANAL_ID> formatında etiketle (Örn: <#1532831582753128530>).
3. ER:LC kodu sorulduğunda doğrudan `piyade` kodunu ve nasıl girileceğini belirt.
4. EĞER SORU YETKİLİ MÜDAHALESİ GEREKTİRİYORSA, ŞİKAYET İÇERİYORSA VEYA ÇÖZÜLEMİYORSA:
   (Üye/oyuncu şikayeti, rol hatası, kural ihlali bildirimi, ban/jail itirazı, yetkili şikayeti, rol isteme veya teknik hata olduğunda)
   Asla kendin karar verme veya tartışma. Doğrudan şu şekilde yetkiliye devret:
   "🛡️ **Yetkili Ekibi Bildirimi:** Bu durum doğrudan yetkili ekibimiz tarafından incelenmektedir. Lütfen video/SS kanıtlarınızı bu kanala iletiniz. Yetkililerimiz en kısa sürede sizinle ilgilenecektir."
5. YETKİLİ ŞİKAYETLERİ VE İÇ KURALLAR: Yetkililere dair iç disiplin kurallarından (Y maddeleri vb.) normal üyelere KESİNLİKLE bahsetme. Yetkili işlemleriyle ilgili şikayet veya itirazlarda doğrudan Üst Yönetim incelemesini belirterek konuyu yetkililere devret.
6. Asla başka oyunların veya sunucuların kurallarını uydurma. Sadece Piyade RP kurallarına sadık kal.
"""

from security import is_prompt_injection, SECURITY_WARNING_REPLY

def get_local_knowledge_reply(prompt: str, user_name: str = "Değerli Üyemiz") -> str | None:
    """
    Gemini API erişilemediğinde veya yanıt geciktiğinde yerel bilgi bankasından
    Piyade RP sistemlerine uygun kusursuz ve anında yanıt üretir.
    """
    # Siber Güvenlik Kontrolü: Prompt injection denemelerini derhal engelle
    if is_prompt_injection(prompt):
        return SECURITY_WARNING_REPLY

    t = prompt.lower().strip()

    # 1. ER:LC Katılım Kodu / Sunucu Kodu
    if any(k in t for k in ["kod", "kodu", "server code", "join code", "nasıl girerim", "nasıl katılırım", "ip"]):
        if any(k in t for k in ["erlc", "er:lc", "oyun", "sunucu", "server", "roblox"]):
            return (
                f"Merhaba **{user_name}**,\n\n"
                f"### 🎮 Piyade RP | ER:LC Katılım Bilgileri\n"
                f"Sunucumuza ER:LC üzerinden katılmak için aşağıdaki adımları izleyebilirsiniz:\n\n"
                f"> 🔑 **Sunucu Katılım Kodu:** `piyade`\n\n"
                f"**Nasıl Katılınır?**\n"
                f"1. Roblox'ta **Emergency Response: Liberty County (ER:LC)** oyununu başlatınız.\n"
                f"2. Ana menüde yer alan **'Servers' (Sunucular)** sekmesine geçiniz.\n"
                f"3. **'Join by Code'** butonuna tıklayıp kutucuğa `piyade` yazınız ve bağlanınız.\n\n"
                f"📌 *Not: Sunucuya girebilmek için Whitelist onayınızın tamamlanmış olması gerekmektedir.*"
            )

    # 2. Kurallar / Sunucu Kuralları / Ceza Sistemi
    if any(k in t for k in ["kural", "kurallar", "kuralları", "ceza", "uyarı", "puan"]):
        if not any(k in t for k in ["rol hatası", "şikayet", "ihlal etti"]):
            return (
                f"Merhaba **{user_name}**,\n\n"
                f"### ⚖️ Piyade Roleplay | Temel Kurallar & Ceza Sistemi\n"
                f"Sunucumuzun huzur ve rol kalitesini korumak adına uygulanan kurallarımız:\n\n"
                f"**📌 Genel Sunucu Kuralları (M Maddeleri):**\n"
                f"• **M1:** Küfür ve hakaret etmek yasaktır. *(2 Ceza Puanı)*\n"
                f"• **M2:** Reklam yapmak ve ticari hesap satışı kesinlikle yasaktır. *(🚨 Kalıcı Ban)*\n"
                f"• **M4:** Taciz içeren davranışlar sergilemek yasaktır. *(2 Gün Timeout)*\n"
                f"• **M5:** Kanalları amacı dışında kullanmak yasaktır. *(3 Ceza Puanı)*\n"
                f"• **M7:** Kasten kavga ortamı yaratmak ve sataşmak yasaktır. *(4 Ceza Puanı)*\n"
                f"• **M8:** Zorbalık yapmak ve üyeleri rahatsız etmek yasaktır. *(5 Ceza Puanı)*\n"
                f"• **M10 / M11:** +18 içerik, ırkçılık ve ayrımcılık yasaktır. *(1 Gün Timeout)*\n"
                f"• **M13:** 3. parti hile, makro ve yazılım kullanımı yasaktır. *(1 Gün Timeout)*\n\n"
                f"**📌 Düzen Kuralları (D Maddeleri):**\n"
                f"• **D1 / D2 / D3:** Duyuru kanallarına flood atmak, ses panelleri ve bot komutlarını spamlamak yasaktır. *(3 Ceza Puanı)*\n\n"
                f"**📊 Ceza Puanı Kademeleri:**\n"
                f"• **3-5 Puan:** Uyarı 1 | **6-8 Puan:** Uyarı 2 | **9-11 Puan:** Uyarı 3\n"
                f"• **10 Puan:** 3 Gün Timeout | **12-14 Puan:** Uyarı 4 | **15+ Puan:** Uyarı 5 + 1 Hafta Jail\n"
                f"• 💡 *30 gün boyunca yeni ceza almayan üyelerin puanları otomatik sıfırlanır.*\n\n"
                f"Detaylı liste için: <#1532828330380890452> (Genel Kurallar) kanalını inceleyebilirsiniz."
            )

    # 3. Rol Terimleri (RP Terimleri)
    if any(k in t for k in ["rp terim", "rol terim", "frp", "fear rp", "rdm", "vdm", "cop bait", "nlr", "combat log", "power gaming", "meta gaming"]):
        return (
            f"Merhaba **{user_name}**,\n\n"
            f"### 🎭 Piyade RP | Temel Roleplay Terimleri\n\n"
            f"• **RM1 — Fail RP (FRP) [3 Puan]:** Mantık dışı rol yapmak (Ağır yaralıyken koşmak vb.).\n"
            f"• **RM2 — Fear RP [3 Puan]:** Can korkusunu rolde hissetmemek (Silah doğrultulmuşken kaçmak vb.).\n"
            f"• **RM3 — Cop Trigger / Cop-Bait [2 Puan]:** Polisi sebepsiz yere kışkırtmak.\n"
            f"• **RM4 — New Life Rule (NLR) [4 Puan]:** Öldükten sonra eski olayı ve katili hatırlamamak kuralı.\n"
            f"• **RM6 — Combat Log (CL) [3 Puan]:** Rolden veya tutuklanmaktan kaçmak için oyundan çıkmak.\n"
            f"• **RM7 — Meta Gaming (MG) [4 Puan]:** Rol dışı bilgiyi (Discord/yayın) rol içine aktarmak.\n"
            f"• **RM8 — Power Gaming (PG) [3 Puan]:** Karşı tarafa tepki hakkı tanımayan imkansız eylemler.\n"
            f"• **RM11 — VDM [3 Puan]:** Aracı bir silah gibi kullanıp insanları ezmek.\n"
            f"• **RM14 — RDM [3 Puan]:** Sebepsizce ve rolsüz adam öldürmek.\n\n"
            f"Tüm terimler ve örnekler için <#1554940447452037192> kanalını ziyaret edebilirsiniz."
        )

    # 4. Kayıt & Whitelist Adımları
    if any(k in t for k in ["kayıt", "kayit", "whitelist", "wl", "başvuru", "basvuru", "nasıl üye", "karakter"]):
        return (
            f"Merhaba **{user_name}**,\n\n"
            f"### 📝 Piyade Roleplay | Adım Adım Kayıt Rehberi\n\n"
            f"Sunucumuzda roleplay deneyimine katılmak için 3 basit adımı tamamlamanız yeterlidir:\n\n"
            f"1️⃣ **İlk Başvuru Formu:**\n"
            f"<#1532831582753128530> kanalına giderek **'Kayıt Ol'** butonuna tıklayınız. Gerçek Ad, Roblox Adı ve Cinsiyet bilgilerinizi giriniz.\n\n"
            f"2️⃣ **Roblox Grubu Doğrulaması:**\n"
            f"Başvurunuz onaylandığında <#1554038042157654016> kanalındaki Roblox Grubumuza katılma isteği atınız ve **'✅ Hesabımı Onayla'** butonuna basınız.\n\n"
            f"3️⃣ **Karakter Formu:**\n"
            f"Kayıt konunuzda beliren **'Karakter Oluştur'** formu ile karakter adı ve yaşınızı (+18) belirleyiniz.\n\n"
            f"🎉 Yetkili onayının ardından **Whitelist** rolünüz teslim edilecek ve sunucuya giriş hakkı kazanacaksınız!"
        )

    # 5. Kanalları Görememe Sorunu
    if any(k in t for k in ["göremiyorum", "goremiyorum", "kanal yok", "kanallar gözükmüyor", "nerede", "bulamadım"]):
        return (
            f"Merhaba **{user_name}**,\n\n"
            f"### 🔍 Kanalları Göremiyorsanız Yapmanız Gerekenler\n\n"
            f"Discord'un sunucu kanallarını gizleme özelliği nedeniyle bazı kanallar sizde kapalı olabilir:\n\n"
            f"1. Discord penceresinin sol üst kısmındaki **'Piyade RP | Los Angeles'** sunucu adına tıklayınız.\n"
            f"2. Açılan menüden **'Tüm Kanalları Göster (Show All Channels)'** seçeneğini işaretleyiniz.\n"
            f"3. Kanallarınız anında görünür hale gelecektir.\n\n"
            f"💡 Ayrıca Whitelist rolünüz yoksa kayıt kanalları dışındaki kısımlar gizlidir. Kayıt olmak için: <#1532831582753128530>"
        )

    # 6. VS / Kapışma Sistemi
    if any(k in t for k in ["vs", "kapışma", "kapisma", "1v1", "düello", "duello"]):
        return (
            f"Merhaba **{user_name}**,\n\n"
            f"### ⚔️ Piyade RP | VS (1v1 Kapışma) Sistemi\n\n"
            f"• **VS Talebi Açma:** <#1537136926287593503> kanalından talep oluşturabilirsiniz.\n"
            f"• **Önemli Kural:** VS kapışmaları roleplay akışından **tamamen bağımsızdır**! Yalnızca bireysel Kademe (Rank) yükseltmek içindir.\n"
            f"• **Türler:** Silahlı düello (PvP) ve Araç kontrolü (Drive).\n"
            f"• **Sonuçlar:** Kazananlar <#1537142672953708685> kanalında duyurulur ve kademe atlar."
        )

    # 7. Çete / Birlik / İllegal
    if any(k in t for k in ["çete", "cete", "birlik", "gang", "kartel", "meth", "soygun"]):
        return (
            f"Merhaba **{user_name}**,\n\n"
            f"### 🏴‍☠️ Piyade RP | Çete & İllegal Sistemleri\n\n"
            f"• **Çete Değiştirme Kuralı:** Bir çeteden ayrılan veya atılan kişi **7 gün** boyunca başka bir çeteye giremez ve çete kuramaz!\n"
            f"• **Meth Üretimi:** İllegal marketten malzeme alınıp üretilir. Hatalı işlemde patlama riski ve polise anında otomatik ihbar gider.\n"
            f"• **Çete Uyarıları:** 3 uyarı alan çete lağvedilir ve bölgesi boşa çıkar.\n"
            f"• **Safezone Kuralı:** Gun Shop, PD, FD, Hastane ve City Spawn alanlarında çatışmak veya soygun yapmak kesinlikle yasaktır."
        )

    return None

