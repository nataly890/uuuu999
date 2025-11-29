import requests
import time
from datetime import datetime

API_KEY = '04fc66143f78496a9832e01b1804e08a'

def monitor_extremos():
    print('MONITOR DE TEMPERATURAS EXTREMAS')
    print('================================')
    
    while True:
        ciudades_extremas = [
            ('Yakutsk,RU', 'Ciudad mas fria'),
            ('Death Valley,US', 'Lugar mas caliente'),
            ('Buenos Aires,AR', 'Tu ciudad'),
            ('Reykjavik,IS', 'Capital nordica')
        ]
        
        print('')
        print('🕒 ' + datetime.now().strftime('%H:%M:%S'))
        print('-' * 40)
        
        for ciudad, descripcion in ciudades_extremas:
            url = 'http://api.openweathermap.org/data/2.5/weather?q=' + ciudad + '&appid=' + API_KEY + '&units=metric'
            response = requests.get(url)
            
            if response.status_code == 200:
                datos = response.json()
                temp = datos['main']['temp']
                nombre = datos['name']
                print(descripcion.ljust(20) + ' | ' + str(round(temp, 1)).rjust(5) + '°C | ' + nombre)
            else:
                print(descripcion.ljust(20) + ' | No disponible')
        
        print('')
        print('Actualizando en 2 minutos... (Ctrl+C para salir)')
        time.sleep(120)

if __name__ == '__main__':
    monitor_extremos()
