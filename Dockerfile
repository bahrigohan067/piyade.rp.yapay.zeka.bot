FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

# Bağımlılıkları yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Proje dosyalarını kopyala
COPY . .

# Botu başlat
CMD ["python", "-u", "main.py"]
