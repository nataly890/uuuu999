from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)

class ClimaAPI:
    def __init__(self):
        self.api_key = "8c78ac9a4d4a9db0f7862c5696560f7a"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def obtener_clima_real(self, ciudad, pais=""):
        try:
            query = f"{ciudad},{pais}" if pais else ciudad
            params = {
                'q': query,
                'appid': self.api_key,
                'units': 'metric',
                'lang': 'es'
            }
            
            response = requests.get(self.base_url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return self._procesar_datos_reales(data)
            else:
                return self._datos_simulados(ciudad, pais)
                
        except Exception as e:
            return self._datos_simulados(ciudad, pais)
    
    def _procesar_datos_reales(self, data):
        icon_map = {
            '01d': 'SOL', '01n': 'LUNA', '02d': 'PARC_NUBLADO', '02n': 'PARC_NUBLADO',
            '03d': 'NUBLADO', '03n': 'NUBLADO', '04d': 'NUBES', '04n': 'NUBES',
            '09d': 'LLUVIA', '09n': 'LLUVIA', '10d': 'LLUVIA_LIGERA', '10n': 'LLUVIA_LIGERA',
            '11d': 'TORMENTA', '11n': 'TORMENTA', '13d': 'NIEVE', '13n': 'NIEVE',
            '50d': 'NIEBLA', '50n': 'NIEBLA'
        }
        
        icon_code = data['weather'][0]['icon']
        icono = icon_map.get(icon_code, 'GLOBO')
        
        return {
            'ciudad': data['name'],
            'pais': data['sys']['country'],
            'temperatura': round(data['main']['temp']),
            'sensacion_termica': round(data['main']['feels_like']),
            'humedad': data['main']['humidity'],
            'presion': data['main']['pressure'],
            'viento': round(data['wind']['speed'], 1),
            'descripcion': data['weather'][0]['description'].title(),
            'icono': icono,
            'actualizado': datetime.now().strftime('%H:%M:%S'),
            'real': True
        }
    
    def _datos_simulados(self, ciudad, pais):
        temp = random.randint(-5, 35)
        
        if temp < 0:
            icono, desc = "FRIO_EXTREMO", "Muy frio"
        elif temp < 10:
            icono, desc = "FRIO", "Frio"
        elif temp < 20:
            icono, desc = "TEMPLADO", "Templado"
        elif temp < 30:
            icono, desc = "CALIDO", "Calido"
        else:
            icono, desc = "CALOR", "Caluroso"
        
        return {
            'ciudad': ciudad,
            'pais': pais,
            'temperatura': temp,
            'sensacion_termica': temp + random.randint(-3, 2),
            'humedad': random.randint(30, 90),
            'presion': random.randint(980, 1030),
            'viento': round(random.uniform(0, 15), 1),
            'descripcion': desc,
            'icono': icono,
            'actualizado': datetime.now().strftime('%H:%M:%S') + " (SIM)",
            'real': False
        }

clima_api = ClimaAPI()

@app.route('/')
def home():
    return jsonify({
        "mensaje": "API del Clima funcionando",
        "endpoints": {
            "/clima/<ciudad>": "Obtener clima de una ciudad",
            "/clima/<ciudad>/<pais>": "Obtener clima de ciudad y pais",
            "/ciudades": "Lista de ciudades disponibles"
        }
    })

@app.route('/clima/<ciudad>')
def obtener_clima_ciudad(ciudad):
    datos = clima_api.obtener_clima_real(ciudad)
    return jsonify(datos)

@app.route('/clima/<ciudad>/<pais>')
def obtener_clima_ciudad_pais(ciudad, pais):
    datos = clima_api.obtener_clima_real(ciudad, pais)
    return jsonify(datos)

@app.route('/ciudades')
def obtener_ciudades():
    ciudades = {
        "Europa": {
            "España": ["Madrid", "Barcelona", "Valencia", "Sevilla"],
            "Francia": ["Paris", "Lyon", "Marsella"],
            "Italia": ["Rome", "Milan", "Naples"]
        },
        "America Norte": {
            "USA": ["New York", "Los Angeles", "Chicago"],
            "Canada": ["Toronto", "Vancouver", "Montreal"],
            "Mexico": ["Mexico City", "Guadalajara", "Monterrey"]
        },
        "America Sur": {
            "Argentina": ["Buenos Aires", "Cordoba", "Rosario"],
            "Brasil": ["Sao Paulo", "Rio de Janeiro", "Brasilia"],
            "Chile": ["Santiago", "Valparaiso", "Concepcion"]
        }
    }
    return jsonify(ciudades)

if __name__ == '__main__':
    print("API DEL CLIMA INICIANDO...")
    print("Servidor corriendo en: http://localhost:5000")
    print("Endpoints disponibles:")
    print("  http://localhost:5000/clima/Madrid")
    print("  http://localhost:5000/clima/New York/USA")
    print("  http://localhost:5000/ciudades")
    app.run(debug=True, host='0.0.0.0', port=5000)
