import requests
import time
from datetime import datetime

API_KEY = "04fc66143f78496a9832e01b1804e08a"

def monitor_temperatura():
    print(" MONITOR DE TEMPERATURAS")
    print("==========================")
    
    ciudad = input("Ciudad a monitorear: ")
    temp_min = float(input("Temperatura mínima alerta: "))
    temp_max = float(input("Temperatura máxima alerta: "))
    
    print("")
    print(f" Monitoreando {ciudad}... (Ctrl+C para detener)")
    print(f" Rango: {temp_min}°C - {temp_max}°C")
    
    try:
        while True:
            url = "http://api.openweathermap.org/data/2.5/weather?q=" + ciudad + "&appid=" + API_KEY + "&units=metric"
            response = requests.get(url)
            
            if response.status_code == 200:
                datos = response.json()
                temp_actual = datos["main"]["temp"]
                hora = datetime.now().strftime("%H:%M:%S")
                
                if temp_actual < temp_min:
                    print(f" {hora} - ALERTA FRÍO: {temp_actual}°C en {datos['name']}")
                elif temp_actual > temp_max:
                    print(f" {hora} - ALERTA CALOR: {temp_actual}°C en {datos['name']}")
                else:
                    print(f" {hora} - {datos['name']}: {temp_actual}°C (Normal)")
            
            time.sleep(300)  # 5 minutos
            
    except KeyboardInterrupt:
        print("")
        print(" Monitoreo detenido")

if __name__ == "__main__":
    monitor_temperatura()
