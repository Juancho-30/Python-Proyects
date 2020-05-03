import time
import os
import pandas

while True:
    if os.path.exists('files/temps_today.csv'):
        data = pandas.read.csv('files/temps_today.csv')
        print(data.mean()) #Promedio de cada una de las columnas
        print(data.mean()['st1']) #Promedio de solo la columna st1
    
    else:
        print('file does not exist')
    time.sleep(10)