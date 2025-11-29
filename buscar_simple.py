import requests

API_KEY = "04fc66143f78496a9832e01b1804e08a"

print("  BUSCADOR SIMPLE - Escribe una ciudad")
print("========================================")

ciudad = input("Ciudad: ")
if ciudad:
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + ciudad + "&appid=" + API_KEY + "&units=metric&lang=es"
    response = requests.get(url)
    if response.status_code == 200:
        datos = response.json()
        print("")
        print(" " + datos["name"] + ", " + datos["sys"]["country"])
        print("  " + str(round(datos["main"]["temp"], 1)) + "°C")
        print("  " + datos["weather"][0]["description"])
        print(" " + str(datos["main"]["humidity"]) + "% humedad")
        print(" " + str(datos["wind"]["speed"]) + " m/s viento")
    else:
        print(" Ciudad no encontrada")
