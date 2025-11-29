import requests
from datetime import datetime

API_KEY = "04fc66143f78496a9832e01b1804e08a"

def reporte_diario():
    ciudades_importantes = [
        "New York,US", "London,GB", "Tokyo,JP", "Sydney,AU", 
        "Buenos Aires,AR", "Dubai,AE", "Moscow,RU", "Cape Town,ZA"
    ]
    
    print(" REPORTE DIARIO DE CLIMA GLOBAL")
    print("=================================")
    print("Fecha: " + datetime.now().strftime("%d/%m/%Y %H:%M"))
    print("")
    
    for ciudad in ciudades_importantes:
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + ciudad + "&appid=" + API_KEY + "&units=metric&lang=es"
        response = requests.get(url)
        
        if response.status_code == 200:
            datos = response.json()
            print(f" {datos['name']:15} | {datos['main']['temp']:5.1f}°C | {datos['weather'][0]['description']:20} | {datos['main']['humidity']}%")
    
    print("")
    print(" Resumen global actualizado")

if __name__ == "__main__":
    reporte_diario()
