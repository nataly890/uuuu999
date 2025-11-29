import requests

API_KEY = "04fc66143f78496a9832e01b1804e08a"

def buscador_personal():
    print("")
    print(" BUSCADOR DE CLIMA PERSONAL")
    print("=============================")
    
    while True:
        print("")
        ciudad = input("  Ingresa el nombre de la ciudad: ").strip()
        if not ciudad:
            break
            
        pais = input(" Ingresa el código del país (opcional - ej: AR, US, MX): ").strip()
        
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
                print(" INFORMACIÓN DEL CLIMA:")
                print(" " + datos["name"] + ", " + datos["sys"]["country"])
                print("  Temperatura: " + str(round(datos["main"]["temp"], 1)) + "°C")
                print(" Sensación térmica: " + str(round(datos["main"]["feels_like"], 1)) + "°C")
                print(" Mínima/Máxima: " + str(round(datos["main"]["temp_min"], 1)) + "°C / " + str(round(datos["main"]["temp_max"], 1)) + "°C")
                print("  Condición: " + datos["weather"][0]["description"].title())
                print(" Humedad: " + str(datos["main"]["humidity"]) + "%")
                print(" Viento: " + str(datos["wind"]["speed"]) + " m/s")
                print(" Presión: " + str(datos["main"]["pressure"]) + " hPa")
                if "visibility" in datos:
                    print("  Visibilidad: " + str(datos["visibility"]/1000) + " km")
            else:
                print("")
                print(" Ciudad no encontrada: " + ciudad)
                print(" Sugerencias:")
                print("   - Verifica la escritura del nombre")
                print("   - Agrega el código del país (ej: Buenos Aires,AR)")
                print("   - Intenta con el nombre en inglés")
                
        except Exception as e:
            print("")
            print(" Error de conexión: " + str(e))
        
        print("")
        continuar = input("¿Buscar otra ciudad? (s/n): ").lower()
        if continuar != "s":
            print("")
            print(" ¡Hasta pronto!")
            break

if __name__ == "__main__":
    buscador_personal()
