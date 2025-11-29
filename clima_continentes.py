import requests
import time
from datetime import datetime

API_KEY = "04fc66143f78496a9832e01b1804e08a"

continentes = {
    "AMÉRICA DEL NORTE": [
        "New York,US", "Los Angeles,US", "Chicago,US", "Toronto,CA", "Mexico City,MX"
    ],
    "AMÉRICA DEL SUR": [
        "Buenos Aires,AR", "Sao Paulo,BR", "Lima,PE", "Santiago,CL", "Bogota,CO"
    ],
    "EUROPA": [
        "London,GB", "Paris,FR", "Madrid,ES", "Rome,IT", "Berlin,DE"
    ],
    "ASIA": [
        "Tokyo,JP", "Beijing,CN", "Seoul,KR", "Singapore,SG", "Dubai,AE"
    ],
    "OCEANÍA Y ÁFRICA": [
        "Sydney,AU", "Auckland,NZ", "Johannesburg,ZA", "Cairo,EG", "Nairobi,KE"
    ]
}

def obtener_clima(ciudad):
    try:
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + ciudad + "&appid=" + API_KEY + "&units=metric&lang=es"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

print("SISTEMA DE CLIMA POR CONTINENTES")
print("================================")

while True:
    hora = datetime.now().strftime("%H:%M:%S")
    print("")
    print(hora + " - CONSULTA GLOBAL")
    print("=" * 40)
    
    for continente, ciudades in continentes.items():
        print("")
        print(continente + ":")
        print("-" * len(continente))
        
        for ciudad in ciudades:
            datos = obtener_clima(ciudad)
            if datos:
                nombre = datos["name"]
                temp = str(round(datos["main"]["temp"], 1))
                desc = datos["weather"][0]["description"]
                print("  " + nombre + ": " + temp + "°C - " + desc)
            else:
                ciudad_nombre = ciudad.split(",")[0]
                print("  " + ciudad_nombre + ": Consultando...")
            
            time.sleep(0.5)
    
    print("")
    print("Actualizando en 2 minutos... (Ctrl+C para salir)")
    time.sleep(120)
