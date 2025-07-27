# Gunakan base image Python resmi
FROM python:3.10-slim

# Set working directory di dalam container
WORKDIR /app

# Salin file requirement dan install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode aplikasi
COPY . .

# Atur variabel environment Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Ekspos port aplikasi
EXPOSE 5000

# Perintah default saat container dijalankan
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
