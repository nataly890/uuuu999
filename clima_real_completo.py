import requests
import time
from datetime import datetime

API_KEY = '04fc66143f78496a9832e01b1804e08a'

def obtener_clima_real(ciudad, pais=''):
    try:
        if pais:
            query = ciudad + ',' + pais
        else:
            query = ciudad
            
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + query + '&appid=' + API_KEY + '&units=metric&lang=es'
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            datos = response.json()
            return {
                'real': True,
                'ciudad': datos['name'],
                'pais': datos['sys']['country'],
                'temperatura': datos['main']['temp'],
                'sensacion': datos['main']['feels_like'],
                'descripcion': datos['weather'][0]['description'].title(),
                'humedad': datos['main']['humidity'],
                'viento': datos['wind']['speed'],
                'presion': datos['main']['pressure'],
                'actualizado': datetime.now().strftime('%H:%M:%S')
            }
        else:
            return {'real': False, 'error': 'Ciudad no encontrada'}
    except Exception as e:
        return {'real': False, 'error': str(e)}

ciudades_globales = [
    ('Buenos Aires', 'AR'), ('Cordoba', 'AR'), ('Rosario', 'AR'),
    ('New York', 'US'), ('Los Angeles', 'US'), ('Chicago', 'US'),
    ('Mexico City', 'MX'), ('Guadalajara', 'MX'), ('Monterrey', 'MX'),
    ('Lima', 'PE'), ('Santiago', 'CL'), ('Bogota', 'CO'),
    ('Sao Paulo', 'BR'), ('Rio de Janeiro', 'BR'), ('Caracas', 'VE'),
    ('London', 'GB'), ('Manchester', 'GB'), ('Paris', 'FR'), ('Lyon', 'FR'),
    ('Madrid', 'ES'), ('Barcelona', 'ES'), ('Valencia', 'ES'),
    ('Rome', 'IT'), ('Milan', 'IT'), ('Berlin', 'DE'), ('Munich', 'DE'),
    ('Tokyo', 'JP'), ('Osaka', 'JP'), ('Seoul', 'KR'),
    ('Beijing', 'CN'), ('Shanghai', 'CN'), ('Hong Kong', 'CN')
]

print('SISTEMA DE CLIMA GLOBAL - DATOS REALES')
print('=' * 60)
print('API Key: ' + API_KEY[:8] + '...')
print('=' * 60)

while True:
    exitosos = 0
    total = len(ciudades_globales)
    
    fecha_actual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    print('')
    print('CONSULTANDO ' + str(total) + ' CIUDADES - ' + fecha_actual)
    print('-' * 60)
    
    for ciudad, pais in ciudades_globales:
        clima = obtener_clima_real(ciudad, pais)
        
        if clima['real']:
            exitosos += 1
            linea = 'OK ' + clima['ciudad'].ljust(18) + ' | ' + str(round(clima['temperatura'], 1)) + 'C | ' + clima['descripcion'].ljust(20) + ' | Hum:' + str(clima['humedad']) + '% | Viento:' + str(clima['viento']) + 'm/s'
            print(linea)
        else:
            print('ERROR ' + ciudad.ljust(18) + ' | ' + clima['error'])
        
        time.sleep(0.5)
    
    print('')
    print('RESULTADO: ' + str(exitosos) + '/' + str(total) + ' ciudades exitosas')
    print('Actualizando en 2 minutos... (Ctrl+C para salir)')
    time.sleep(120)
