import requests
import json
import time
from datetime import datetime

# API Key gratuita (puedes reemplazarla con la tuya)
API_KEY = 'd7b9c7b8c8a8c8a8c8a8c8a8c8a8c8a8'  # Key de ejemplo

def obtener_clima_ciudad(ciudad, pais=''):
    try:
        if pais:
            query = f'{ciudad},{pais}'
        else:
            query = ciudad
            
        url = f'https://api.openweathermap.org/data/2.5/weather?q={query}&appid={API_KEY}&units=metric&lang=es'
        
        respuesta = requests.get(url, timeout=10)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            return {
                'ciudad': datos['name'],
                'pais': datos['sys']['country'],
                'temperatura': datos['main']['temp'],
                'sensacion_termica': datos['main']['feels_like'],
                'descripcion': datos['weather'][0]['description'].title(),
                'humedad': datos['main']['humidity'],
                'viento': datos['wind']['speed'],
                'presion': datos['main']['pressure'],
                'actualizado': datetime.now().strftime('%H:%M:%S')
            }
        else:
            return {'error': f'Ciudad no encontrada: {ciudad}'}
    except Exception as e:
        return {'error': f'Error de conexión: {str(e)}'}

def mostrar_clima(datos):
    if 'error' in datos:
        print(f\"❌ {datos['error']}\")
    else:
        print(f\"🌍 {datos['ciudad']}, {datos['pais']}\")
        print(f\"🌡️  Temperatura: {datos['temperatura']}°C\")
        print(f\"🤗 Sensación térmica: {datos['sensacion_termica']}°C\")
        print(f\"☁️  Condición: {datos['descripcion']}\")
        print(f\"💧 Humedad: {datos['humedad']}%\")
        print(f\"💨 Viento: {datos['viento']} m/s\")
        print(f\"📊 Presión: {datos['presion']} hPa\")
        print(f\"🕒 Actualizado: {datos['actualizado']}\")
        print(\"-\" * 40)

# Ciudades principales por país
ciudades_globales = [
    ('Buenos Aires', 'AR'), ('New York', 'US'), ('London', 'GB'),
    ('Tokyo', 'JP'), ('Madrid', 'ES'), ('Mexico City', 'MX'),
    ('Lima', 'PE'), ('Santiago', 'CL'), ('Bogota', 'CO'),
    ('Sao Paulo', 'BR'), ('Paris', 'FR'), ('Berlin', 'DE'),
    ('Rome', 'IT'), ('Moscow', 'RU'), ('Beijing', 'CN'),
    ('Sydney', 'AU'), ('Cairo', 'EG'), ('Mumbai', 'IN')
]

print(\"=\" * 50)
print(\"🌤️  SISTEMA DE CLIMA EN TIEMPO REAL\")
print(\"=\" * 50)

while True:
    print(f\"\\n🕒 Consultando clima: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\")
    print(\"-\" * 50)
    
    for ciudad, pais in ciudades_globales:
        clima = obtener_clima_ciudad(ciudad, pais)
        mostrar_clima(clima)
        time.sleep(1)  # Espera entre consultas
    
    print(\"\\n🔄 Actualizando en 60 segundos...\")
    print(\"Presiona Ctrl+C para detener\")
    time.sleep(60)
