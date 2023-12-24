# Esta parte es para crear una imagen de nginx, importando la ultima version de nginx usando la sintaxis de docker
FROM nginx:latest

# Esto es para copiar el contenido de la carpeta sitio a la carpeta de nginx, en la carpeta sitio esta nuestro index.html el cual es el que se va a mostrar en el navegador
# Path: /usr/share/nginx/html
COPY /sitio /usr/share/nginx/html

# Esto crea un volumen en el contenedor para que se pueda acceder a el desde afuera
VOLUME ["sitio", "/usr/share/nginx/html"]