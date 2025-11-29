import requests
import json

def obtener_clima_ciudad(ciudad):
    try:
        # API de OpenWeatherMap (gratuita)
        api_key = 'tu_api_key_aqui'  # Necesitas registrarte en openweathermap.org
        url = f'http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es'
        
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            return {
                'ciudad': datos['name'],
                'pais': datos['sys']['country'],
                'temperatura': datos['main']['temp'],
                'descripcion': datos['weather'][0]['description'],
                'humedad': datos['main']['humidity'],
                'viento': datos['wind']['speed']
            }
        else:
            return None
    except:
        return None

# Lista de países y ciudades principales (ejemplo extendido)
paises_ciudades = {
    'Argentina': ['Buenos Aires', 'Córdoba', 'Rosario', 'Mendoza', 'La Plata'],
    'México': ['Ciudad de México', 'Guadalajara', 'Monterrey', 'Puebla', 'Cancún'],
    'España': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao'],
    'Colombia': ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena'],
    'Perú': ['Lima', 'Arequipa', 'Trujillo', 'Cusco', 'Chiclayo']
}

print('=== CLIMA EN TIEMPO REAL ===')
for pais, ciudades in paises_ciudades.items():
    print(f'\n--- {pais} ---')
    for ciudad in ciudades:
        clima = obtener_clima_ciudad(ciudad)
        if clima:
            print(f'{ciudad}: {clima[\"temperatura\"]}°C, {clima[\"descripcion\"]}')
        else:
            print(f'{ciudad}: Datos no disponibles')

print('\n⚠️  Para usar esta API, necesitas:')
print('1. Registrarte en: https://openweathermap.org/api')
print('2. Obtener una API key gratuita')
print('3. Reemplazar \"tu_api_key_aqui\" con tu key real')
