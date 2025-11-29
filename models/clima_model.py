import requests
import random
from datetime import datetime

class ClimaModel:
    def __init__(self):
        self.api_key = "8c78ac9a4d4a9db0f7862c5696560f7a"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
        self.continentes_data = self._cargar_continentes()
    
    def _cargar_continentes(self):
        return {
            "Europa": {
                "España": ["Madrid", "Barcelona", "Valencia", "Sevilla", "Zaragoza"],
                "Francia": ["Paris", "Marsella", "Lyon", "Toulouse", "Niza"],
                "Italia": ["Roma", "Milán", "Nápoles", "Turín", "Palermo"],
                "Alemania": ["Berlín", "Hamburgo", "Múnich", "Colonia", "Frankfurt"]
            },
            "America Norte": {
                "Estados Unidos": ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"],
                "Canada": ["Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa"],
                "Mexico": ["Ciudad de Mexico", "Guadalajara", "Monterrey", "Puebla", "Toluca"]
            },
            "America Sur": {
                "Argentina": ["Buenos Aires", "Córdoba", "Rosario", "Mendoza", "La Plata"],
                "Brasil": ["Sao Paulo", "Río de Janeiro", "Brasilia", "Salvador", "Fortaleza"],
                "Chile": ["Santiago", "Valparaíso", "Concepción", "La Serena", "Antofagasta"]
            },
            "Asia": {
                "China": ["Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Chengdu"],
                "Japon": ["Tokio", "Osaka", "Kyoto", "Yokohama", "Nagoya"],
                "India": ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad"]
            },
            "Africa": {
                "Egipto": ["El Cairo", "Alejandría", "Giza", "Shubra", "Port Said"],
                "Nigeria": ["Lagos", "Kano", "Ibadan", "Kaduna", "Port Harcourt"],
                "Sudafrica": ["Johannesburgo", "Ciudad del Cabo", "Durban", "Pretoria", "Port Elizabeth"]
            }
        }
    
    def obtener_continentes(self):
        return list(self.continentes_data.keys())
    
    def obtener_paises(self, continente):
        return list(self.continentes_data.get(continente, {}).keys())
    
    def obtener_ciudades(self, continente, pais):
        return self.continentes_data.get(continente, {}).get(pais, [])
    
    def obtener_clima(self, ciudad, pais=""):
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
