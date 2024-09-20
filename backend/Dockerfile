# Usar una imagen base de Python
FROM python:3.9-alpine

# Instalar dependencias del sistema necesarias para psycopg2
RUN apk update && apk add --no-cache \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de código
COPY app.py app.py

# Instalar dependencias directamente
RUN pip install --upgrade pip && \
    pip install Flask==2.0.2 psycopg2-binary==2.9.1

# Exponer el puerto
EXPOSE 5000

# Ejecutar la aplicación
CMD ["python", "app.py"]
