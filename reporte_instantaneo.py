import requests
from datetime import datetime

API_KEY = '04fc66143f78496a9832e01b1804e08a'

def reporte_instantaneo():
    ciudades_clave = [
        'Buenos Aires,AR', 'New York,US', 'London,GB', 'Tokyo,JP', 
        'Sydney,AU', 'Dubai,AE', 'Cape Town,ZA'
    ]
    
    print('REPORTE INSTANTANEO - CIUDADES CLAVE')
    print('====================================')
    print('Hora: ' + datetime.now().strftime('%H:%M:%S'))
    print('')
    
    for ciudad in ciudades_clave:
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + ciudad + '&appid=' + API_KEY + '&units=metric&lang=es'
        response = requests.get(url)
        
        if response.status_code == 200:
            datos = response.json()
            temp = datos['main']['temp']
            # Iconos según temperatura
            icono = '🔥' if temp > 30 else '❄️' if temp < 10 else '🌡️'
            nombre = datos['name']
            descripcion = datos['weather'][0]['description']
            print(icono + ' ' + nombre.ljust(15) + ' | ' + str(round(temp, 1)).rjust(5) + '°C | ' + descripcion)

if __name__ == '__main__':
    reporte_instantaneo()
