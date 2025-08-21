# /api/Dockerfile
FROM python:3.9-slim

# Instala o cliente do postgres para o script de espera
RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Copia o script para dentro da imagem
COPY wait-for-db.sh .
RUN chmod +x wait-for-db.sh

# Executa o script de espera antes de iniciar a API
CMD ["./wait-for-db.sh", "db", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]