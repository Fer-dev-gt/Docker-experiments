# Este programa es un ejemplo de como crear un servidor web con Flask, es una API generada con Python

import json
from flask import Flask         # Import Flask to allow us to create our app
app = Flask(__name__)           # Create a new instance of the Flask class called "app"

@app.route('/getMyInfo')        # The "@" decorator associates this route with the function immediately following
def getMyInfo():      
  value = {                     # Creamos un objeto con la información que queremos retornar
    "name": "Amin",
    "lastname": "Espinoza",
    "socialMedia":
    [
      {"facebookUser": "aminespinoza10"},
      {"instagramUser": "aminespinoza10"},
      {"xUser": "aminespinoza"},
      {"linkedin": "amin-espinoza"},
      {"githubUser": "aminespinoza10"}
    ],
    "blog": "https://aminespinoza.com",
    "author": "Fernando Orozco"
  }
  return json.dumps(value)    # Retornamos el valor en formato JSON el cual es un string de un Objeto