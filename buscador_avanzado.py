import requests

API_KEY = "04fc66143f78496a9832e01b1804e08a"

# Ciudades populares para sugerencias
ciudades_populares = {
    "Buenos Aires": "AR",
    "New York": "US", 
    "London": "GB",
    "Tokyo": "JP",
    "Madrid": "ES",
    "Paris": "FR",
    "Berlin": "DE",
    "Rome": "IT",
    "Sydney": "AU",
    "Moscow": "RU",
    "Beijing": "CN",
    "Dubai": "AE",
    "Mumbai": "IN",
    "Cairo": "EG",
    "Johannesburg": "ZA"
}

def buscador_con_sugerencias():
    print("")
    print("  BUSCADOR DE CLIMA CON SUGERENCIAS")
    print("=====================================")
    print("")
    print("Ciudades populares disponibles:")
    print("-" * 30)
    
    for i, ciudad in enumerate(ciudades_populares.keys(), 1):
        print(f"{i}. {ciudad}")
    
    print("")
    print("También puedes escribir cualquier ciudad del mundo")
    print("")
    
    while True:
        print("Opciones:")
        print("1. Escribir nombre de ciudad")
        print("2. Usar lista de ciudades populares") 
        print("3. Salir")
        
        opcion = input("Selecciona una opción (1-3): ").strip()
        
        if opcion == "1":
            buscar_ciudad_manual()
        elif opcion == "2":
            buscar_ciudad_lista()
        elif opcion == "3":
            print(" ¡Hasta pronto!")
            break
        else:
            print(" Opción no válida")

def buscar_ciudad_manual():
    print("")
    ciudad = input("  Nombre de la ciudad: ").strip()
    if not ciudad:
        return
        
    pais = input(" Código de país (opcional): ").strip()
    consultar_clima(ciudad, pais)

def buscar_ciudad_lista():
    print("")
    print("Ciudades populares:")
    ciudades_lista = list(ciudades_populares.keys())
    for i, ciudad in enumerate(ciudades_lista, 1):
        print(f"{i}. {ciudad}")
    
    try:
        seleccion = int(input("Selecciona un número: ")) - 1
        if 0 <= seleccion < len(ciudades_lista):
            ciudad = ciudades_lista[seleccion]
            pais = ciudades_populares[ciudad]
            consultar_clima(ciudad, pais)
        else:
            print(" Selección no válida")
    except:
        print(" Ingresa un número válido")

def consultar_clima(ciudad, pais=""):
    if pais:
        query = ciudad + "," + pais
    else:
        query = ciudad
        
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + query + "&appid=" + API_KEY + "&units=metric&lang=es"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            datos = response.json()
            print("")
            print(" CLIMA ENCONTRADO:")
            print(" " + datos["name"] + ", " + datos["sys"]["country"])
            print("  Temperatura: " + str(round(datos["main"]["temp"], 1)) + "°C")
            print(" Sensación: " + str(round(datos["main"]["feels_like"], 1)) + "°C")
            print("  Condición: " + datos["weather"][0]["description"].title())
            print(" Humedad: " + str(datos["main"]["humidity"]) + "%")
            print(" Viento: " + str(datos["wind"]["speed"]) + " m/s")
        else:
            print("")
            print(" Ciudad no encontrada: " + ciudad)
    except Exception as e:
        print("")
        print(" Error: " + str(e))

if __name__ == "__main__":
    buscador_con_sugerencias()
