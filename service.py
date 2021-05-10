#!flask/bin/python
from flask import Flask
from predecir import predecir 

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>San Francisco Pronostico</h1></br><a href='http://0.0.0.0:5000/v1/prediccion/24horas/'>Predicción de 24 horas</a></br><a href='http://0.0.0.0:5000/v1/prediccion/48horas/'>Predicción de 48 horas</a></br><a href='http://0.0.0.0:5000/v1/prediccion/72horas/'>Predicción de 72 horas</a>",200

@app.route('/v1/prediccion/24horas/')
def pronostico24():
    salida = predecir(24)
    return salida ,200

@app.route('/v1/prediccion/48horas/')
def pronostico48():
    salida = predecir(48)
    return salida ,200

@app.route('/v1/prediccion/72horas/')
def pronostico72():
    salida = predecir(72)
    return salida ,200

if __name__ == '__main__':
    app.run(debug=True)