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
COPY backend.py backend.py

# Instalar solo psycopg2
RUN pip install --upgrade pip && pip install psycopg2-binary==2.9.1

# Exponer el puerto 5000
EXPOSE 5000

# Ejecutar la aplicación
CMD ["python", "backend.py"]
