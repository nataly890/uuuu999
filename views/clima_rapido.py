import requests

API_KEY = "04fc66143f78496a9832e01b1804e08a"

def clima_rapido():
    ciudades = ["Buenos Aires,AR", "New York,US", "London,GB", "Tokyo,JP", "Madrid,ES"]
    
    print("")
    print("⚡ CLIMA RÁPIDO - CIUDADES FRECUENTES")
    print("====================================")
    
    for ciudad in ciudades:
        url = "http://api.openweathermap.org/data/2.5/weather?q=" + ciudad + "&appid=" + API_KEY + "&units=metric&lang=es"
        response = requests.get(url)
        if response.status_code == 200:
            datos = response.json()
            print("📍 " + datos["name"] + ": " + str(round(datos["main"]["temp"], 1)) + "°C - " + datos["weather"][0]["description"])
        else:
            print("❌ " + ciudad.split(",")[0] + ": No disponible")

if __name__ == "__main__":
    clima_rapido()
