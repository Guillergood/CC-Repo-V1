import pandas as lectorCsv
import pymongo
from pymongo import MongoClient
from statsmodels.tsa.arima_model import ARIMA
import pmdarima as pm
import joblib as jb


def crearModelo():

    # How to connect with MongoClient https://mongodb.github.io/node-mongodb-native/driver-articles/mongoclient.html
    # https://stackoverflow.com/questions/40346767/pymongo-auth-failed-in-python-script
    client = MongoClient('mongodb://%s:%s@0.0.0.0:27017' % ('admin', 'admin'))
    baseDatos = client["SanFrancisco"]
    columna = baseDatos["Pronostico"]
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
    marcoDeDatos = lectorCsv.DataFrame(list(columna.find()))
    marcoDeDatos = marcoDeDatos[['datetime','Temperatura','Humedad']]

    # https://pypi.org/project/pmdarima/
    modeloTemperatura = pm.auto_arima(marcoDeDatos[['Temperatura']], start_p=1, start_q=1,
                        test='adf',       # use adftest to find optimal 'd'
                        max_p=3, max_q=3, # maximum p and q
                        m=1,              # frequency of series
                        d=None,           # let model determine 'd'
                        seasonal=False,   # No Seasonality
                        start_P=0, 
                        D=0, 
                        trace=True,
                        error_action='ignore',  
                        suppress_warnings=True, 
                        stepwise=True)
    # Guardar el modelo https://scikit-learn.org/stable/modules/model_persistence.html
    jb.dump(modeloTemperatura, './modeloTemperatura.pkl')

    modeloHumedad = pm.auto_arima(marcoDeDatos[['Humedad']], start_p=1, start_q=1,
                        test='adf',       # use adftest to find optimal 'd'
                        max_p=3, max_q=3, # maximum p and q
                        m=1,              # frequency of series
                        d=None,           # let model determine 'd'
                        seasonal=False,   # No Seasonality
                        start_P=0, 
                        D=0, 
                        trace=True,
                        error_action='ignore',  
                        suppress_warnings=True, 
                        stepwise=True)
                        
    # Guardar el modelo https://scikit-learn.org/stable/modules/model_persistence.html
    jb.dump(modeloHumedad, './modeloHumedad.pkl')

if __name__ == '__main__':
    crearModelo()