import requests

API_KEY = '04fc66143f78496a9832e01b1804e08a'

print('CLIMA SIMPLE')
print('============')

ciudades = ['Buenos Aires,AR', 'New York,US', 'London,GB']

for ciudad in ciudades:
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + ciudad + '&appid=' + API_KEY + '&units=metric&lang=es'
    response = requests.get(url)
    
    if response.status_code == 200:
        datos = response.json()
        print(datos['name'] + ': ' + str(datos['main']['temp']) + 'C - ' + datos['weather'][0]['description'])
    else:
        print(ciudad + ': Error')
