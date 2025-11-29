from ..services.weather_api.weather_service import APIManager
from ..models.ciudad_model import Ciudad

class ClimaController:
    def __init__(self):
        self.api_manager = APIManager()
    
    def buscar_clima(self, nombre_ciudad):
        if not nombre_ciudad or not nombre_ciudad.strip():
            return None
        
        return self.api_manager.buscar_clima(nombre_ciudad.strip())
    
    def formatear_datos_clima(self, ciudad):
        if not ciudad:
            return None
        
        return {
            'header': f\"{ciudad.nombre}, {ciudad.pais}\",
            'temperatura': f\"{ciudad.temperatura}°C\",
            'humedad': f\"{ciudad.humedad}%\",
            'viento': f\"{ciudad.viento} km/h\",
            'descripcion': ciudad.descripcion,
            'fecha_actualizacion': datetime.now().strftime('%H:%M:%S')
        }
