# server/FileHandler/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copiamos e instalamos dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos la aplicación
COPY . .

# Exponemos el puerto 5001 para Flask
EXPOSE 5001

CMD ["python", "app.py"]
