# 🤖 Piyade Roleplay — Yapay Zeka Destek Botu (Piyade AI)

Bu proje, **Piyade Roleplay (PRP | Los Angeles)** sunucusundaki bilet (ticket) kanallarında 7/24 kesintisiz, akıllı ve profesyonel destek sağlayan **Google Gemini** destekli yapay zeka asistanıdır.

---

## ✨ Özellikler

1. **Akıllı Bilet Algılama**:
   - Ana bot tarafından açılan `ticket-{kullanıcı_adı}` formatındaki kanalları ve `acan_id:` topic etiketlerini anında tespit eder.
2. **Kişiselleştirilmiş Karşılama**:
   - Bilet açıldığında kullanıcıyı etiketleyerek: *"Size nasıl yardımcı olabiliriz?"* sorusuyla zarif ve kurumsal bir karşılama mesajı gönderir.
3. **Açık Mavi "Düşünüyor..." Durumu**:
   - Kullanıcı sorusunu sorduğu anda açık mavi tonundaki arayüzde `🌀 Düşünüyor...` bildirimini ve Discord yazıyor animasyonunu gösterir.
4. **Piyade RP Bilgi Bankası ile Kusursuz Yanıtlar**:
   - Sunucu kuralları (M1-M13, D1-D3, RM1-RM17), ceza puanları, 3 aşamalı kayıt sistemi, Roblox grubu doğrulama, ekonomi ve safezonelar hakkında hatasız ve detaylı bilgi sunar.
5. **Yetkili Ekibine Devir (Eskalasyon)**:
   - Eğer konu yetki gerektiren bir durumsa (ban itirazı, rol talebi, şikayet veya çözülemeyen teknik aksaklıklar):
     `"🛡️ Yetkililerimiz en kısa sürede sizinle ilgilenecektir."` mesajını açık mavi embed içinde vurgular.
6. **İnteraktif Butonlar**:
   - `🛎️ Yetkili Çağır`: Ticket yetkilisini pingleyerek bildirim iletir.
   - `✅ Sorunum Çözüldü`: Teşekkür mesajı ile süreci sonlandırır.

---

## 🚀 Kurulum ve Çalıştırma

### 1. Gereksinimler
Sistemde Python 3.10+ yüklü olmalıdır.

```bash
python -m pip install -r requirements.txt
```

### 2. .env Dosyasını Doldurun
`.env` dosyasını açıp aşağıdaki bilgileri giriniz:
```env
TOKEN_AL_BOT=discord_bot_tokeniniz_buraya
GEMINI_API_KEY=gemini_api_keyiniz_buraya
GEMINI_MODEL=gemini-2.5-flash
GUILD_ID=1529545898294509589
```

### 3. Botu Başlatın
```bash
python main.py
```