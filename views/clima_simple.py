import requests
import json

def obtener_clima_gratis(ciudad):
    try:
        # API alternativa (puede tener limitaciones)
        url = f'https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid=demo_key&units=metric'
        respuesta = requests.get(url, timeout=10)
        
        if respuesta.status_code == 200:
            datos = respuesta.json()
            return {
                'ciudad': datos['name'],
                'temperatura': datos['main']['temp'],
                'descripcion': datos['weather'][0]['description']
            }
    except:
        pass
    return None

# Ciudades para probar
ciudades = ['London', 'New York', 'Tokyo', 'Paris', 'Madrid', 'Buenos Aires', 'Mexico City', 'Lima', 'Santiago']

print('Clima en ciudades principales:')
for ciudad in ciudades:
    clima = obtener_clima_gratis(ciudad)
    if clima:
        print(f'{clima[\"ciudad\"]}: {clima[\"temperatura\"]}°C, {clima[\"descripcion\"]}')
    else:
        print(f'{ciudad}: Consultando...')
