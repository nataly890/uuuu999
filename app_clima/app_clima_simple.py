import flet as ft
import requests
from datetime import datetime

class ClimaGlobalReal:
    def __init__(self):
        self.api_key = "8c78ac9a4d4a9db0f7862c5696560f7a"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def obtener_clima_real(self, ciudad, pais=""):
        try:
            query = f"{ciudad},{pais}" if pais else ciudad
            params = {
                'q': query,
                'appid': self.api_key,
                'units': 'metric',
                'lang': 'es'
            }
            
            response = requests.get(self.base_url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return self._procesar_datos_reales(data)
            else:
                return self._datos_simulados(ciudad, pais)
                
        except Exception as e:
            return self._datos_simulados(ciudad, pais)
    
    def _procesar_datos_reales(self, data):
        icon_map = {
            '01d': '☀️', '01n': '🌙', '02d': '⛅', '02n': '⛅',
            '03d': '☁️', '03n': '☁️', '04d': '☁️', '04n': '☁️',
            '09d': '🌧️', '09n': '🌧️', '10d': '🌦️', '10n': '🌦️',
            '11d': '⛈️', '11n': '⛈️', '13d': '❄️', '13n': '❄️',
            '50d': '🌫️', '50n': '🌫️'
        }
        
        icon_code = data['weather'][0]['icon']
        icono = icon_map.get(icon_code, '🌍')
        
        return {
            'ciudad': data['name'],
            'pais': data['sys']['country'],
            'temperatura': round(data['main']['temp']),
            'sensacion_termica': round(data['main']['feels_like']),
            'humedad': data['main']['humidity'],
            'presion': data['main']['pressure'],
            'viento': round(data['wind']['speed'], 1),
            'descripcion': data['weather'][0]['description'].title(),
            'icono': icono,
            'actualizado': datetime.now().strftime('%H:%M:%S'),
            'real': True
        }
    
    def _datos_simulados(self, ciudad, pais):
        import random
        temp = random.randint(-5, 35)
        
        if temp < 0:
            icono, desc = "❄️", "Muy frio"
        elif temp < 10:
            icono, desc = "🥶", "Frio"
        elif temp < 20:
            icono, desc = "⛅", "Templado"
        elif temp < 30:
            icono, desc = "☀️", "Calido"
        else:
            icono, desc = "🔥", "Caluroso"
        
        return {
            'ciudad': ciudad,
            'pais': pais,
            'temperatura': temp,
            'sensacion_termica': temp + random.randint(-3, 2),
            'humedad': random.randint(30, 90),
            'presion': random.randint(980, 1030),
            'viento': round(random.uniform(0, 15), 1),
            'descripcion': desc,
            'icono': icono,
            'actualizado': datetime.now().strftime('%H:%M:%S') + " (SIM)",
            'real': False
        }

CONTINENTES = {
    "Europa": {
        "España": ["Madrid", "Barcelona", "Valencia"],
        "Francia": ["Paris", "Lyon", "Marsella"],
        "Italia": ["Rome", "Milan", "Naples"]
    },
    "America Norte": {
        "USA": ["New York", "Los Angeles", "Chicago"],
        "Canada": ["Toronto", "Vancouver", "Montreal"],
        "Mexico": ["Mexico City", "Guadalajara", "Monterrey"]
    },
    "America Sur": {
        "Argentina": ["Buenos Aires", "Cordoba", "Rosario"],
        "Brasil": ["Sao Paulo", "Rio de Janeiro", "Brasilia"],
        "Chile": ["Santiago", "Valparaiso", "Concepcion"]
    },
    "Asia": {
        "China": ["Beijing", "Shanghai", "Guangzhou"],
        "Japon": ["Tokyo", "Osaka", "Kyoto"],
        "India": ["Mumbai", "Delhi", "Bangalore"]
    }
}

def main(page):
    page.title = "Clima Global"
    page.padding = 10
    page.scroll = ft.ScrollMode.ADAPTIVE
    
    app_clima = ClimaGlobalReal()
    
    header = ft.Container(
        content=ft.Column([
            ft.Text("CLIMA GLOBAL", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Datos en Tiempo Real", size=14)
        ]),
        padding=15
    )
    
    panel_continentes = ft.Column(scroll=ft.ScrollMode.ADAPTIVE)
    
    panel_resultado = ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text("Selecciona una ciudad", size=16)
            ]),
            padding=20
        ),
        visible=False
    )
    
    progreso = ft.ProgressRing(visible=False)
    
    def crear_boton_ciudad(ciudad, pais):
        return ft.TextButton(
            content=ft.Container(
                content=ft.Row([
                    ft.Text(ciudad, size=14),
                    ft.Icon(ft.icons.ARROW_FORWARD_IOS, size=14)
                ]),
                padding=10
            ),
            on_click=lambda e, c=ciudad, p=pais: buscar_ciudad(c, p)
        )
    
    def mostrar_continente(continente_nombre):
        panel_continentes.controls.clear()
        
        for pais, ciudades in CONTINENTES[continente_nombre].items():
            panel_continentes.controls.append(
                ft.Container(
                    content=ft.Text(pais, size=16, weight=ft.FontWeight.BOLD),
                    padding=10
                )
            )
            
            for ciudad in ciudades:
                panel_continentes.controls.append(
                    crear_boton_ciudad(ciudad, pais)
                )
        
        page.update()
    
    def buscar_ciudad(ciudad, pais):
        progreso.visible = True
        panel_resultado.visible = False
        page.update()
        
        datos = app_clima.obtener_clima_real(ciudad, pais)
        
        progreso.visible = False
        
        if datos:
            mostrar_resultado(datos)
        else:
            mostrar_error("Error")
    
    def mostrar_resultado(datos):
        panel_resultado.content.content.controls = [
            ft.Row([
                ft.Text(datos['icono'], size=28),
                ft.Column([
                    ft.Text(datos['ciudad'], size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(datos['pais'], size=14)
                ])
            ]),
            
            ft.Divider(height=15),
            
            ft.Row([
                ft.Text(f"{datos['temperatura']}°", size=36, weight=ft.FontWeight.BOLD),
                ft.Column([
                    ft.Text(datos['descripcion'], size=16),
                    ft.Text(f"Sensacion: {datos['sensacion_termica']}°C", size=12)
                ])
            ]),
            
            ft.Divider(height=20),
            
            ft.Row([
                ft.Column([
                    ft.Text("HUMEDAD"),
                    ft.Text(f"{datos['humedad']}%", size=16, weight=ft.FontWeight.BOLD)
                ]),
                
                ft.Column([
                    ft.Text("VIENTO"),
                    ft.Text(f"{datos['viento']} m/s", size=16, weight=ft.FontWeight.BOLD)
                ]),
                
                ft.Column([
                    ft.Text("PRESION"),
                    ft.Text(f"{datos['presion']} hPa", size=14, weight=ft.FontWeight.BOLD)
                ])
            ]),
            
            ft.Divider(height=15),
            
            ft.Text(f"Actualizado: {datos['actualizado']}", size=12)
        ]
        
        panel_resultado.visible = True
        page.update()
    
    def mostrar_error(mensaje):
        panel_resultado.content.content.controls = [
            ft.Icon(ft.icons.ERROR, size=40),
            ft.Text("Error", size=18, weight=ft.FontWeight.BOLD),
            ft.Text(mensaje)
        ]
        panel_resultado.visible = True
        page.update()
    
    botones_continentes = ft.Row(scroll=ft.ScrollMode.ADAPTIVE)
    for continente in CONTINENTES.keys():
        boton = ft.ElevatedButton(
            content=ft.Text(continente),
            on_click=lambda e, c=continente: mostrar_continente(c)
        )
        botones_continentes.controls.append(boton)
    
    page.add(
        ft.Column([
            header,
            ft.Text("Selecciona continente:", size=16),
            botones_continentes,
            ft.Divider(height=20),
            ft.Text("Ciudades:", size=16),
            panel_continentes,
            ft.Divider(height=20),
            progreso,
            panel_resultado
        ], scroll=ft.ScrollMode.ADAPTIVE)
    )
    
    mostrar_continente("Europa")

ft.app(target=main)
