import requests
import time
from datetime import datetime

API_KEY = '04fc66143f78496a9832e01b1804e08a'

ciudades = ['Buenos Aires', 'New York', 'London', 'Tokyo', 'Madrid']

def obtener_clima(ciudad):
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + ciudad + '&appid=' + API_KEY + '&units=metric&lang=es'
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

print('SISTEMA DE CLIMA')
print('===============')

while True:
    hora = datetime.now().strftime('%H:%M:%S')
    print('')
    print(hora + ' - Consultando clima...')
    print('-' * 30)
    
    for ciudad in ciudades:
        datos = obtener_clima(ciudad)
        if datos:
            print(datos['name'] + ': ' + str(datos['main']['temp']) + '°C - ' + datos['weather'][0]['description'])
        else:
            print(ciudad + ': No disponible')
    
    print('')
    print('Actualizando en 60 segundos...')
    time.sleep(60)
