import requests

API_KEY = "04fc66143f78496a9832e01b1804e08a"

def menu_principal():
    while True:
        print("")
        print("🌎 BUSCADOR DE CLIMA - MENÚ PRINCIPAL")
        print("=====================================")
        print("1. Buscar ciudad manualmente")
        print("2. Ciudades de América")
        print("3. Ciudades de Europa") 
        print("4. Ciudades de Asia")
        print("5. Salir")
        
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            buscar_manual()
        elif opcion == "2":
            mostrar_america()
        elif opcion == "3":
            mostrar_europa()
        elif opcion == "4":
            mostrar_asia()
        elif opcion == "5":
            print("👋 ¡Hasta pronto!")
            break
        else:
            print("❌ Opción no válida")

def buscar_manual():
    print("")
    ciudad = input("🏙️  Ciudad: ")
    if ciudad:
        pais = input("🌍 País (opcional): ")
        consultar_clima(ciudad, pais)

def mostrar_america():
    ciudades = [
        ("Buenos Aires", "AR"),
        ("New York", "US"),
        ("Mexico City", "MX"),
        ("Lima", "PE"),
        ("Santiago", "CL"),
        ("Bogota", "CO"),
        ("Sao Paulo", "BR")
    ]
    print("")
    print("🌎 AMÉRICA:")
    print("-----------")
    for ciudad, pais in ciudades:
        consultar_clima(ciudad, pais)

def mostrar_europa():
    ciudades = [
        ("London", "GB"),
        ("Paris", "FR"),
        ("Madrid", "ES"),
        ("Rome", "IT"),
        ("Berlin", "DE"),
        ("Amsterdam", "NL")
    ]
    print("")
    print("🌍 EUROPA:")
    print("----------")
    for ciudad, pais in ciudades:
        consultar_clima(ciudad, pais)

def mostrar_asia():
    ciudades = [
        ("Tokyo", "JP"),
        ("Beijing", "CN"),
        ("Seoul", "KR"),
        ("Singapore", "SG"),
        ("Dubai", "AE"),
        ("Mumbai", "IN")
    ]
    print("")
    print("🌏 ASIA:")
    print("--------")
    for ciudad, pais in ciudades:
        consultar_clima(ciudad, pais)

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
            print("📍 " + datos["name"] + ": " + str(round(datos["main"]["temp"], 1)) + "°C - " + datos["weather"][0]["description"])
        else:
            print("❌ " + ciudad + ": No encontrada")
    except:
        print("❌ " + ciudad + ": Error de conexión")

if __name__ == "__main__":
    menu_principal()
