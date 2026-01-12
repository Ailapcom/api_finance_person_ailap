# Builder stage
FROM python:3.11-slim as builder

WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements
COPY requirements.txt .

# Instalar dependencias Python con --user para que vayan a /root/.local
RUN pip install --user --no-cache-dir -r requirements.txt

# Final stage
FROM python:3.11-slim

WORKDIR /app

# Instalar solo las dependencias runtime necesarias
RUN apt-get update && apt-get install -y \
    libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Copiar dependencias Python instaladas
COPY --from=builder /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copiar código de la aplicación
COPY . .

# Crear directorio de logs con permisos
RUN mkdir -p /app/logs && chmod 755 /app/logs

# Crear usuario no-root
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser

ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]