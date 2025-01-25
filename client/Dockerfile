# client/Dockerfile
FROM nginx:stable-alpine

# Copiamos el contenido estático al directorio por defecto de Nginx
COPY . /usr/share/nginx/html

# Exponemos el puerto 80 (dentro del contenedor)
EXPOSE 80

# Nginx se ejecuta por defecto como CMD