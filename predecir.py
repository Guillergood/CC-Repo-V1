import pandas as lectorCsv
from datetime import datetime
from statsmodels.tsa.arima_model import ARIMA
import numpy as np
import joblib as jb


def predecir(n):

    # Carga modelos https://joblib.readthedocs.io/en/latest/persistence.html
    modeloTemperatura = jb.load('./modeloTemperatura.pkl')
    modeloHumedad = jb.load('./modeloHumedad.pkl')
    
    # Intervalo de confianza https://github.com/manuparra/MaterialCC2020/blob/master/exampleARIMA_humidity.py
    prediccionTemperatura, confint = modeloTemperatura.predict(n_periods=n, return_conf_int=True)
    prediccionHumedad, confint = modeloHumedad.predict(n_periods=n, return_conf_int=True)
    
    hoy = datetime.now()
    indice = lectorCsv.date_range(hoy, periods=n, freq='H')

    datosPrediccion = lectorCsv.DataFrame(index=indice, columns=['Hora','Temperatura','Humedad'])
    # Crear array https://numpy.org/doc/stable/reference/generated/numpy.array.html
    temperatura = np.array(prediccionTemperatura)
    humedad = np.array(prediccionHumedad)
    datosPrediccion['Hora'] = indice.strftime('%B %d, %Y, %r')
    datosPrediccion['Temperatura'] = temperatura
    datosPrediccion['Humedad'] = humedad

    return datosPrediccion.to_json(orient='records')
