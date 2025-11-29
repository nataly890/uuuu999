from flask import Flask, jsonify
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
        return {
            'ciudad': data['name'],
            'pais': data['sys']['country'],
            'temperatura': round(data['main']['temp']),
            'sensacion_termica': round(data['main']['feels_like']),
            'humedad': data['main']['humidity'],
            'presion': data['main']['pressure'],
            'viento': round(data['wind']['speed'], 1),
            'descripcion': data['weather'][0]['description'].title(),
            'actualizado': datetime.now().strftime('%H:%M:%S'),
            'real': True
        }
    
    def _datos_simulados(self, ciudad, pais):
        temp = random.randint(-10, 40)
        return {
            'ciudad': ciudad,
            'pais': pais,
            'temperatura': temp,
            'sensacion_termica': temp + random.randint(-5, 5),
            'humedad': random.randint(20, 95),
            'presion': random.randint(980, 1040),
            'viento': round(random.uniform(0, 25), 1),
            'descripcion': random.choice(['Soleado', 'Nublado', 'Lluvioso', 'Ventoso']),
            'actualizado': datetime.now().strftime('%H:%M:%S') + ' (SIM)',
            'real': False
        }

clima_api = ClimaAPI()

CONTINENTES_DATA = {
    "Europa": {
        "España": ["Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza", "Málaga"],
        "Francia": ["Paris", "Marsella", "Lyon", "Toulouse", "Niza", "Nantes"],
        "Italia": ["Roma", "Milán", "Nápoles", "Turín", "Palermo", "Génova"],
        "Alemania": ["Berlín", "Hamburgo", "Múnich", "Colonia", "Frankfurt", "Stuttgart"],
        "Reino Unido": ["Londres", "Birmingham", "Glasgow", "Liverpool", "Bristol", "Mánchester"]
    },
    "América del Norte": {
        "Estados Unidos": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"],
        "Canadá": ["Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa", "Edmonton"],
        "México": ["Ciudad de México", "Guadalajara", "Monterrey", "Puebla", "Toluca", "Tijuana"]
    },
    "América del Sur": {
        "Argentina": ["Buenos Aires", "Córdoba", "Rosario", "Mendoza", "La Plata", "Mar del Plata"],
        "Brasil": ["Sao Paulo", "Río de Janeiro", "Brasilia", "Salvador", "Fortaleza", "Belo Horizonte"],
        "Chile": ["Santiago", "Valparaíso", "Concepción", "La Serena", "Antofagasta", "Temuco"]
    },
    "Asia": {
        "China": ["Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Chengdu", "Wuhan"],
        "Japón": ["Tokio", "Osaka", "Kyoto", "Yokohama", "Nagoya", "Sapporo"],
        "India": ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai"]
    },
    "África": {
        "Egipto": ["El Cairo", "Alejandría", "Giza", "Shubra", "Port Said", "Suez"],
        "Nigeria": ["Lagos", "Kano", "Ibadan", "Kaduna", "Port Harcourt", "Benin"],
        "Sudáfrica": ["Johannesburgo", "Ciudad del Cabo", "Durban", "Pretoria", "Port Elizabeth", "Bloemfontein"]
    }
}

@app.route('/')
def home():
    return jsonify({"mensaje": "API Clima Global", "version": "1.0"})

@app.route('/clima/<ciudad>')
def clima_ciudad(ciudad):
    datos = clima_api.obtener_clima_real(ciudad)
    return jsonify(datos)

@app.route('/clima/<ciudad>/<pais>')
def clima_ciudad_pais(ciudad, pais):
    datos = clima_api.obtener_clima_real(ciudad, pais)
    return jsonify(datos)

@app.route('/continentes')
def continentes():
    return jsonify(CONTINENTES_DATA)

@app.route('/ciudades/<continente>')
def ciudades_continente(continente):
    return jsonify(CONTINENTES_DATA.get(continente, {}))

if __name__ == '__main__':
    print("API CLIMA GLOBAL INICIADA")
    print("URL: http://localhost:5000")
    app.run(debug=True, port=5000)
