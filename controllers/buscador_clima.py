import requests
import json

API_KEY = 'd7b9c7b8c8a8c8a8c8a8c8a8c8a8c8a8'

def buscar_clima():
    print(\"🔍 BUSCADOR DE CLIMA GLOBAL\")
    print(\"=\" * 40)
    
    while True:
        ciudad = input(\"\\n🏙️  Ingresa el nombre de la ciudad (o 'salir' para terminar): \")
        
        if ciudad.lower() == 'salir':
            break
            
        pais = input(\"🌍 Ingresa el código del país (opcional - ej: AR, US, MX): \")
        
        if ciudad:
            try:
                if pais:
                    query = f'{ciudad},{pais}'
                else:
                    query = ciudad
                    
                url = f'http://api.openweathermap.org/data/2.5/weather?q={query}&appid={API_KEY}&units=metric&lang=es'
                respuesta = requests.get(url)
                
                if respuesta.status_code == 200:
                    datos = respuesta.json()
                    print(f\"\\n✅ CLIMA ENCONTRADO:\")
                    print(f\"📍 Ciudad: {datos['name']}, {datos['sys']['country']}\")
                    print(f\"🌡️  Temperatura: {datos['main']['temp']}°C\")
                    print(f\"🤗 Sensación: {datos['main']['feels_like']}°C\")
                    print(f\"☁️  Condición: {datos['weather'][0]['description'].title()}\")
                    print(f\"💧 Humedad: {datos['main']['humidity']}%\")
                    print(f\"💨 Viento: {datos['wind']['speed']} m/s\")
                else:
                    print(\"❌ Ciudad no encontrada. Intenta con otro nombre.\")
                    
            except Exception as e:
                print(f\"❌ Error de conexión: {e}\")

if __name__ == \"__main__\":
    buscar_clima()
