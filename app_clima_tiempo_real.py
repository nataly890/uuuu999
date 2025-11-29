import flet as ft
import requests
import json
from datetime import datetime

def main(page: ft.Page):
    page.title = "Sistema de Clima Global - Tiempo Real"
    page.padding = 50
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # TU API KEY REAL
    API_KEY = "04fc66143f78496a9832e01b1804e08a"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    # Componentes de la UI
    titulo = ft.Text("🌤️ Clima en Tiempo Real", size=35, weight=ft.FontWeight.BOLD)
    
    ciudad_input = ft.TextField(
        label="Ciudad",
        hint_text="Ej: Madrid, Tokyo, New York, Lima",
        width=400,
        autofocus=True
    )
    
    resultado_text = ft.Text("Ingresa una ciudad y presiona Buscar", size=16, selectable=True)
    loading_indicator = ft.ProgressRing(visible=False)
    ultima_actualizacion = ft.Text("", size=12, color=ft.colors.GREY_600)
    
    def obtener_clima_real(ciudad):
        try:
            params = {
                'q': ciudad,
                'appid': API_KEY,
                'units': 'metric',
                'lang': 'es'
            }
            
            response = requests.get(BASE_URL, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return {
                    'ciudad': data['name'],
                    'pais': data['sys']['country'],
                    'temperatura': round(data['main']['temp']),
                    'sensacion_termica': round(data['main']['feels_like']),
                    'descripcion': data['weather'][0]['description'].title(),
                    'humedad': data['main']['humidity'],
                    'presion': data['main']['pressure'],
                    'viento': round(data['wind']['speed'] * 3.6),
                    'icono': data['weather'][0]['icon']
                }
            else:
                return None
                
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def buscar_clima(e):
        ciudad = ciudad_input.value.strip()
        if not ciudad:
            resultado_text.value = "⚠️ Por favor, ingresa una ciudad"
            page.update()
            return
        
        # Mostrar loading
        loading_indicator.visible = True
        resultado_text.value = f"🔍 Buscando clima en tiempo real para: {ciudad}..."
        page.update()
        
        # Obtener datos reales
        datos_clima = obtener_clima_real(ciudad)
        
        # Ocultar loading
        loading_indicator.visible = False
        
        if datos_clima:
            # Emojis según el clima
            emoji_clima = {
                'clear': '☀️',
                'clouds': '☁️',
                'rain': '🌧️',
                'snow': '❄️',
                'thunderstorm': '⛈️',
                'drizzle': '🌦️',
                'mist': '🌫️',
                'default': '🌤️'
            }
            
            icono = datos_clima['icono']
            emoji = emoji_clima.get(icono[:-1], emoji_clima['default'])
            
            resultado_text.value = f"""{emoji} **Clima en {datos_clima['ciudad']}, {datos_clima['pais']}**

🌡️ **Temperatura:** {datos_clima['temperatura']}°C
🤔 **Sensación térmica:** {datos_clima['sensacion_termica']}°C
☁️ **Condición:** {datos_clima['descripcion']}
💧 **Humedad:** {datos_clima['humedad']}%
📊 **Presión:** {datos_clima['presion']} hPa
💨 **Viento:** {datos_clima['viento']} km/h
"""
            ultima_actualizacion.value = f"🕐 Actualizado: {datetime.now().strftime('%H:%M:%S')}"
        else:
            resultado_text.value = "❌ Error: Ciudad no encontrada o problema de conexión"
            ultima_actualizacion.value = ""
        
        page.update()
    
    buscar_btn = ft.ElevatedButton(
        "Buscar Clima en Tiempo Real",
        on_click=buscar_clima,
        icon=ft.icons.SEARCH,
        style=ft.ButtonStyle(
            color=ft.colors.WHITE,
            bgcolor=ft.colors.BLUE_600
        )
    )
    
    # Layout
    page.add(
        ft.Column([
            titulo,
            ft.Container(height=20),
            ciudad_input,
            ft.Container(height=15),
            ft.Row([buscar_btn, loading_indicator], alignment=ft.MainAxisAlignment.CENTER),
            ft.Container(height=30),
            resultado_text,
            ft.Container(height=10),
            ultima_actualizacion
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

if __name__ == "__main__":
    ft.app(target=main)
