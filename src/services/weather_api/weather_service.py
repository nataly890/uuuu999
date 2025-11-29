import requests
from datetime import datetime
from ..models.ciudad_model import Ciudad, Configuracion

class WeatherAPI:
    def __init__(self):
        self.config = Configuracion()
        self.base_url = \"http://api.openweathermap.org/data/2.5/weather\"
    
    def obtener_clima_ciudad(self, nombre_ciudad):
        try:
            params = {
                'q': nombre_ciudad,
                'appid': self.config.api_key,
                'units': self.config.unidades,
                'lang': self.config.idioma
            }
            
            response = requests.get(self.base_url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return Ciudad(
                    nombre=data['name'],
                    pais=data['sys']['country'],
                    temperatura=round(data['main']['temp']),
                    humedad=data['main']['humidity'],
                    viento=round(data['wind']['speed'] * 3.6),
                    descripcion=data['weather'][0]['description'].title()
                )
            return None
        except Exception as e:
            print(f\"Error API: {e}\")
            return None

class APIManager:
    def __init__(self):
        self.weather_api = WeatherAPI()
    
    def buscar_clima(self, ciudad):
        return self.weather_api.obtener_clima_ciudad(ciudad)
