# Usar una imagen base de Python
FROM python:3.9-alpine

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos y código
COPY requirements.txt requirements.txt
COPY app.py app.py

# Instalar dependencias
RUN pip install -r requirements.txt

# Exponer el puerto
EXPOSE 5000

# Ejecutar la aplicación
CMD ["python", "app.py"]
