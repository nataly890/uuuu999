import requests
from datetime import datetime

API_KEY = '04fc66143f78496a9832e01b1804e08a'

def comparar_continentes():
    continentes = {
        'AMERICA': ['Buenos Aires,AR', 'New York,US', 'Mexico City,MX'],
        'EUROPA': ['London,GB', 'Madrid,ES', 'Moscow,RU'],
        'ASIA': ['Tokyo,JP', 'Dubai,AE', 'Singapore,SG'],
        'OCEANIA': ['Sydney,AU', 'Auckland,NZ']
    }
    
    print('COMPARADOR DE CONTINENTES')
    print('=========================')
    print('Fecha: ' + datetime.now().strftime('%d/%m/%Y %H:%M'))
    print('')
    
    for continente, ciudades in continentes.items():
        print(continente + ':')
        print('-' * len(continente))
        
        temps = []
        for ciudad in ciudades:
            url = 'http://api.openweathermap.org/data/2.5/weather?q=' + ciudad + '&appid=' + API_KEY + '&units=metric&lang=es'
            response = requests.get(url)
            
            if response.status_code == 200:
                datos = response.json()
                temp = datos['main']['temp']
                temps.append(temp)
                nombre = datos['name']
                print('  ' + nombre + ': ' + str(round(temp, 1)) + '°C')
        
        if temps:
            promedio = sum(temps) / len(temps)
            print('  -> Promedio: ' + str(round(promedio, 1)) + '°C')
        print('')

if __name__ == '__main__':
    comparar_continentes()
