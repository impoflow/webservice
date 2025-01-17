# server/ApiHandler/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Si tienes un requirements.txt, lo copias y lo instalas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto de la aplicación
COPY . .

# Exponemos el puerto 5000 para Flask
EXPOSE 5000

# Ejecutamos la app (ajusta si tu archivo principal se llama distinto)
CMD ["python", "app.py"]
