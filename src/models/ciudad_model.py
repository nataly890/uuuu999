class Ciudad:
    def __init__(self, nombre, pais, temperatura, humedad, viento, descripcion):
        self.nombre = nombre
        self.pais = pais
        self.temperatura = temperatura
        self.humedad = humedad
        self.viento = viento
        self.descripcion = descripcion
    
    def to_dict(self):
        return {
            'ciudad': self.nombre,
            'pais': self.pais,
            'temperatura': self.temperatura,
            'humedad': self.humedad,
            'viento': self.viento,
            'descripcion': self.descripcion
        }

class Configuracion:
    def __init__(self):
        self.api_key = \"04fc66143f78496a9832e01b1804e08a\"
        self.unidades = \"metric\"
        self.idioma = \"es\"
