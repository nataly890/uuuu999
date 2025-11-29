import requests
import time
from datetime import datetime

API_KEY = '04fc66143f78496a9832e01b1804e08a'

# 50+ CIUDADES GLOBALES
ciudades = [
    # América del Norte
    'New York,US', 'Los Angeles,US', 'Chicago,US', 'Houston,US', 'Phoenix,US',
    'Toronto,CA', 'Vancouver,CA', 'Montreal,CA', 'Mexico City,MX', 'Guadalajara,MX',
    
    # América Central y Caribe
    'Panama City,PA', 'San Jose,CR', 'San Juan,PR', 'Havana,CU', 'Santo Domingo,DO',
    
    # América del Sur
    'Buenos Aires,AR', 'Cordoba,AR', 'Rosario,AR', 'Sao Paulo,BR', 'Rio de Janeiro,BR',
    'Lima,PE', 'Santiago,CL', 'Bogota,CO', 'Caracas,VE', 'Quito,EC',
    
    # Europa
    'London,GB', 'Manchester,GB', 'Paris,FR', 'Lyon,FR', 'Madrid,ES', 'Barcelona,ES',
    'Rome,IT', 'Milan,IT', 'Berlin,DE', 'Munich,DE', 'Amsterdam,NL', 'Brussels,BE',
    'Vienna,AT', 'Zurich,CH', 'Stockholm,SE', 'Oslo,NO', 'Copenhagen,DK',
    
    # Asia
    'Tokyo,JP', 'Osaka,JP', 'Seoul,KR', 'Beijing,CN', 'Shanghai,CN', 'Hong Kong,CN',
    'Singapore,SG', 'Bangkok,TH', 'Kuala Lumpur,MY', 'Mumbai,IN', 'Delhi,IN',
    'Dubai,AE', 'Istanbul,TR', 'Tel Aviv,IL', 'Riyadh,SA',
    
    # Oceanía y África
    'Sydney,AU', 'Melbourne,AU', 'Auckland,NZ', 'Johannesburg,ZA', 'Cape Town,ZA',
    'Cairo,EG', 'Lagos,NG', 'Nairobi,KE', 'Casablanca,MA', 'Accra,GH'
]

def obtener_clima(ciudad):
    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q=' + ciudad + '&appid=' + API_KEY + '&units=metric&lang=es'
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

print('SISTEMA DE CLIMA GLOBAL - 50+ CIUDADES')
print('=======================================')
print('Total de ciudades: ' + str(len(ciudades)))
print('API Key: ' + API_KEY[:8] + '...')
print('=======================================')

while True:
    hora = datetime.now().strftime('%H:%M:%S')
    exitosos = 0
    total = len(ciudades)
    
    print('')
    print(hora + ' - Consultando ' + str(total) + ' ciudades...')
    print('-' * 50)
    
    for ciudad in ciudades:
        datos = obtener_clima(ciudad)
        if datos:
            exitosos += 1
            nombre_ciudad = datos['name']
            temp = str(round(datos['main']['temp'], 1))
            desc = datos['weather'][0]['description']
            print(nombre_ciudad + ': ' + temp + '°C - ' + desc)
        else:
            ciudad_nombre = ciudad.split(',')[0]
            print(ciudad_nombre + ': No disponible')
        
        time.sleep(0.3)  # Pausa para no saturar API
    
    print('')
    print('RESULTADO: ' + str(exitosos) + '/' + str(total) + ' ciudades con datos')
    porcentaje = (exitosos / total) * 100
    print('EFICACIA: ' + str(round(porcentaje, 1)) + '%')
    print('')
    print('Actualizando en 3 minutos... (Ctrl+C para salir)')
    time.sleep(180)
