# Esta linea indica la imagen base que vamos a utilizar en nuestro contenedor
FROM python:3.12.0-alpine3.18

# Esta linea indica el directorio de trabajo dentro del contenedor el cual se creara si no existe, lo llamaremos app
WORKDIR /app

# Esta linea copia el archivo requirements.txt del directorio actual al directorio de trabajo del contenedor el cual se creo en la linea anterior y es llamado app
COPY requirements.txt requirements.txt

# Esta linea ejecuta el comando pip install -r requirements.txt dentro del contenedor
RUN pip install -r requirements.txt

# Esta linea copia todo el contenido del directorio actual al directorio de trabajo del contenedor el cual se creo en la linea anterior y es llamado app
COPY . .

# Esta linea nos permite ejecutar el comando python -m flask run --host=
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
