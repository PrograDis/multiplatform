# Usa una imagen ligera de Python
FROM python:3.10-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de tu app
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expón el puerto que usará la app
EXPOSE 8000

# Comando para ejecutar la app
CMD ["python", "app.py"]
