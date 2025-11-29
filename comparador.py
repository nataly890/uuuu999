import requests

API_KEY = "04fc66143f78496a9832e01b1804e08a"

def comparar_ciudades():
    print(" COMPARADOR DE CLIMAS")
    print("======================")
    
    ciudades = []
    
    while True:
        print("")
        ciudad = input("Agrega una ciudad para comparar (o 'fin' para terminar): ")
        if ciudad.lower() == 'fin':
            break
        if ciudad:
            ciudades.append(ciudad)
            print(f" {ciudad} agregada. Total: {len(ciudades)} ciudades")
    
    if ciudades:
        print("")
        print(" COMPARACIÓN:")
        print("=" * 50)
        
        for ciudad in ciudades:
            url = "http://api.openweathermap.org/data/2.5/weather?q=" + ciudad + "&appid=" + API_KEY + "&units=metric&lang=es"
            response = requests.get(url)
            
            if response.status_code == 200:
                datos = response.json()
                print(f" {datos['name']:15} | {str(round(datos['main']['temp'], 1)):5}°C | {datos['weather'][0]['description']:20} | {datos['main']['humidity']}%")
            else:
                print(f" {ciudad:15} | No encontrada")

if __name__ == "__main__":
    comparar_ciudades()
