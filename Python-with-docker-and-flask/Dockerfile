# Esto sirve para definir la imagen base del contenedor, en este caso la imagen base es 'python:3.12-alpine3.17'
FROM python:3.12-alpine3.17

# Esto sirve para definir el directorio de trabajo dentro del contenedor, en este caso el directorio de trabajo es '/app'
WORKDIR /app

# Esto sirve para copiar archivos de la maquina local al contenedor, en este caso copiamos el archivo 'requirements.txt' al contenedor
COPY requirements.txt requirements.txt

# Esto sirve para ejecutar comandos en el contenedor, dentro del archivo 'requirements.txt' se encuentran las dependencias de la app que van a ser instaladas en el contenedor
RUN pip install -r requirements.txt       

# Copiamos los archivos de la maquina local al contenedor que seria la carpeta '/app'
COPY . .

# Definimos un comando que se va a ejecutar cuando el contenedor se inicie, en este caso el comando es 'python -m flask run --host=
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]