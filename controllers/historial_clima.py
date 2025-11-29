import requests
import datetime

API_KEY = "04fc66143f78496a9832e01b1804e08a"

historial = []

def buscar_con_historial():
    print(" BUSCADOR CON HISTORIAL")
    print("========================")
    
    while True:
        print("")
        print("1. Buscar ciudad")
        print("2. Ver historial")
        print("3. Limpiar historial")
        print("4. Salir")
        
        opcion = input("Opción: ")
        
        if opcion == "1":
            ciudad = input("Ciudad: ")
            if ciudad:
                resultado = consultar_clima(ciudad)
                historial.append({
                    "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "ciudad": ciudad,
                    "resultado": resultado
                })
        elif opcion == "2":
            mostrar_historial()
        elif opcion == "3":
            historial.clear()
            print(" Historial limpiado")
        elif opcion == "4":
            break
        else:
            print(" Opción no válida")

def consultar_clima(ciudad):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + ciudad + "&appid=" + API_KEY + "&units=metric&lang=es"
    response = requests.get(url)
    
    if response.status_code == 200:
        datos = response.json()
        info = datos["name"] + ": " + str(round(datos["main"]["temp"], 1)) + "°C - " + datos["weather"][0]["description"]
        print(" " + info)
        return info
    else:
        print(" Ciudad no encontrada")
        return "No encontrada"

def mostrar_historial():
    print("")
    print(" HISTORIAL DE BÚSQUEDAS")
    print("=========================")
    if not historial:
        print("No hay búsquedas en el historial")
    else:
        for i, busqueda in enumerate(historial, 1):
            print(f"{i}. {busqueda['fecha']} - {busqueda['ciudad']}: {busqueda['resultado']}")

if __name__ == "__main__":
    buscar_con_historial()
