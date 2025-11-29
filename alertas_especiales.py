import requests
import time
from datetime import datetime

API_KEY = "04fc66143f78496a9832e01b1804e08a"

def alertas_especiales():
    print("🚨 SISTEMA DE ALERTAS ESPECIALES")
    print("================================")
    
    alertas = {
        "CALOR EXTREMO": {"ciudad": "Dubai,AE", "limite": 35},
        "FRÍO EXTREMO": {"ciudad": "Beijing,CN", "limite": -5},
        "LLUVIA INTENSA": {"ciudad": "Singapore,SG", "condicion": "rain"},
        "VIENTO FUERTE": {"ciudad": "Chicago,US", "limite_viento": 15}
    }
    
    while True:
        print("")
        print("🕒 " + datetime.now().strftime("%H:%M:%S") + " - Verificando alertas...")
        print("-" * 40)
        
        for tipo, config in alertas.items():
            url = "http://api.openweathermap.org/data/2.5/weather?q=" + config["ciudad"] + "&appid=" + API_KEY + "&units=metric&lang=es"
            response = requests.get(url)
            
            if response.status_code == 200:
                datos = response.json()
                temp = datos["main"]["temp"]
                desc = datos["weather"][0]["description"].lower()
                viento = datos["wind"]["speed"]
                
                if "limite" in config and temp > config["limite"]:
                    print(f"🚨 {tipo}: {datos['name']} - {temp}°C (Límite: {config['limite']}°C)")
                elif "condicion" in config and config["condicion"] in desc:
                    print(f"🚨 {tipo}: {datos['name']} - {desc}")
                elif "limite_viento" in config and viento > config["limite_viento"]:
                    print(f"🚨 {tipo}: {datos['name']} - Viento: {viento} m/s")
                else:
                    print(f"✅ {tipo}: {datos['name']} - Normal")
            else:
                print(f"❌ {tipo}: Error en consulta")
        
        print("")
        print("🔍 Próxima verificación en 5 minutos...")
        time.sleep(300)

if __name__ == "__main__":
    alertas_especiales()
