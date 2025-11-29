from models.clima_model import ClimaModel

class ClimaController:
    def __init__(self):
        self.model = ClimaModel()
    
    def obtener_continentes(self):
        return self.model.obtener_continentes()
    
    def obtener_paises(self, continente):
        return self.model.obtener_paises(continente)
    
    def obtener_ciudades(self, continente, pais):
        return self.model.obtener_ciudades(continente, pais)
    
    def obtener_clima_ciudad(self, ciudad, pais=""):
        return self.model.obtener_clima(ciudad, pais)
    
    def validar_ciudad(self, ciudad):
        return len(ciudad.strip()) > 0
