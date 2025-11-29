import requests
import time
from datetime import datetime

API_KEY = "04fc66143f78496a9832e01b1804e08a"

continentes = {
    "AMÉRICA DEL NORTE": [
        "New York,US", "Los Angeles,US", "Chicago,US", "Toronto,CA", "Mexico City,MX",
        "Miami,US", "Vancouver,CA", "Houston,US", "Phoenix,US"
    ],
    "AMÉRICA DEL SUR": [
        "Buenos Aires,AR", "Sao Paulo,BR", "Rio de Janeiro,BR", "Lima,PE", "Santiago,CL",
        "Bogota,CO", "Caracas,VE", "Quito,EC", "Montevideo,UY"
    ],
    "EUROPA": [
        "London,GB", "Paris,FR", "Madrid,ES", "Barcelona,ES", "Rome,IT", 
        "Milan,IT", "Berlin,DE", "Amsterdam,NL", "Brussels,BE", "Vienna,AT"
    ],
    "ASIA": [
        "Tokyo,JP", "Osaka,JP", "Beijing,CN", "Shanghai,CN", "Seoul,KR",
        "Singapore,SG", "Dubai,AE", "Bangkok,TH", "Mumbai,IN", "Delhi,IN"
    ],
    "OCEANÍA": [
        "Sydney,AU", "Melbourne,AU", "Auckland,NZ", "Brisbane,AU", "Perth,AU"
    ],
    "ÁFRICA": [
        "Johannesburg,ZA", "Cape Town,ZA", "Cairo,EG", "Nairobi,KE", "Casablanca,MA",
        "Lagos,NG", "Accra,GH", "Addis Ababa,ET"
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

print("🌎 SISTEMA DE CLIMA GLOBAL EXPANDIDO")
print("====================================")
print("Total ciudades: " + str(sum(len(c) for c in continentes.values())))
print("API Key: " + API_KEY[:8] + "...")
print("====================================")

while True:
    hora = datetime.now().strftime("%H:%M:%S")
    exitosos = 0
    total = sum(len(ciudades) for ciudades in continentes.values())
    
    print("")
    print(hora + " - CONSULTANDO " + str(total) + " CIUDADES")
    print("=" * 50)
    
    for continente, ciudades in continentes.items():
        print("")
        print(continente + " (" + str(len(ciudades)) + " ciudades):")
        print("-" * (len(continente) + 15))
        
        cont_exitosos = 0
        for ciudad in ciudades:
            datos = obtener_clima(ciudad)
            if datos:
                exitosos += 1
                cont_exitosos += 1
                print("  " + datos["name"] + ": " + str(round(datos["main"]["temp"], 1)) + "°C - " + datos["weather"][0]["description"])
            else:
                print("  " + ciudad.split(",")[0] + ": Consultando...")
            
            time.sleep(0.3)
        
        print("  → " + str(cont_exitosos) + "/" + str(len(ciudades)) + " exitosas")
    
    porcentaje = (exitosos / total) * 100
    print("")
    print("📊 GLOBAL: " + str(exitosos) + "/" + str(total) + " ciudades (" + str(round(porcentaje, 1)) + "%)")
    print("")
    print("🔄 Actualizando en 3 minutos... (Ctrl+C para salir)")
    time.sleep(180)
