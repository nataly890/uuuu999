import requests
import time
from datetime import datetime

# === REEMPLAZA ESTA KEY CON LA TUYA ===
API_KEY = "PEGA_AQUI_TU_API_KEY_GRATUITA"

def clima_real(ciudad, pais=""):
    \"\"\"Obtiene datos REALES de clima con API key válida\"\"\"
    try:
        if pais:
            query = f'{ciudad},{pais}'
        else:
            query = ciudad
            
        url = f'http://api.openweathermap.org/data/2.5/weather?q={query}&appid={API_KEY}&units=metric&lang=es'
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
                'presion': datos['main']['pressure']
            }
        else:
            return {'real': False, 'error': 'Ciudad no encontrada'}
    except Exception as e:
        return {'real': False, 'error': str(e)}

# Ciudades globales para monitorear
ciudades = [
    ('Buenos Aires', 'AR'), ('New York', 'US'), ('London', 'GB'),
    ('Tokyo', 'JP'), ('Madrid', 'ES'), ('Mexico City', 'MX'),
    ('Lima', 'PE'), ('Santiago', 'CL'), ('Bogota', 'CO'),
    ('Sao Paulo', 'BR'), ('Paris', 'FR'), ('Berlin', 'DE')
]

print('🌤️  SISTEMA DE CLIMA REAL - CON API KEY')
print('=' * 60)

if API_KEY == "PEGA_AQUI_TU_API_KEY_GRATUITA":
    print('❌ CONFIGURACIÓN REQUERIDA:')
    print('1. Obtén tu API Key gratuita en: https://home.openweathermap.org/users/sign_up')
    print('2. Reemplaza "PEGA_AQUI_TU_API_KEY_GRATUITA" con tu key real')
    print('3. Vuelve a ejecutar este script')
else:
    while True:
        exitosos = 0
        total = len(ciudades)
        
        print(f'\n📊 CLIMA REAL - {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
        print('-' * 60)
        
        for ciudad, pais in ciudades:
            clima = clima_real(ciudad, pais)
            
            if clima['real']:
                exitosos += 1
                print(f'✅ {ciudad:15} | {clima[\"temperatura\"]:5.1f}°C | {clima[\"descripcion\"]:20} | 💧{clima[\"humedad\"]}%')
            else:
                print(f'❌ {ciudad:15} | Error: {clima[\"error\"]}')
            
            time.sleep(1)  # Pausa para no exceder límites
        
        print(f'\n📈 Estadísticas: {exitosos}/{total} ciudades con datos reales')
        print('🔄 Actualizando en 2 minutos... (Ctrl+C para salir)')
        time.sleep(120)
