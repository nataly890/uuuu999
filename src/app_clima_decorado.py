import flet as ft
import requests
import json
from datetime import datetime

def main(page: ft.Page):
    page.title = "🌍 Clima Global Pro - Tiempo Real"
    page.padding = 30
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.BLUE_GREY_50
    page.scroll = ft.ScrollMode.ADAPTIVE
    
    # API KEY REAL
    API_KEY = "04fc66143f78496a9832e01b1804e08a"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    # Colores y estilos
    COLOR_PRIMARIO = ft.colors.BLUE_900
    COLOR_SECUNDARIO = ft.colors.CYAN_700
    
    # Componentes de la UI decorados
    header = ft.Container(
        content=ft.Column([
            ft.Text("🌤️", size=50),
            ft.Text("CLIMA GLOBAL PRO", 
                   size=28, 
                   weight=ft.FontWeight.BOLD,
                   color=COLOR_PRIMARIO),
            ft.Text("Datos meteorológicos en tiempo real", 
                   size=16, 
                   color=ft.colors.GREY_600),
        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
        padding=20,
        margin=ft.margin.only(bottom=20)
    )
    
    card_busqueda = ft.Card(
        elevation=8,
        content=ft.Container(
            content=ft.Column([
                ft.Text("🔍 Buscar Ciudad", 
                       size=20, 
                       weight=ft.FontWeight.BOLD,
                       color=COLOR_PRIMARIO),
                ft.Container(height=10),
                ciudad_input := ft.TextField(
                    label="Nombre de la ciudad",
                    hint_text="Ej: Madrid, Tokyo, New York, Lima...",
                    width=400,
                    autofocus=True,
                    border_color=COLOR_PRIMARIO,
                    prefix_icon=ft.icons.LOCATION_ON
                ),
                ft.Container(height=15),
                ft.Row([
                    buscar_btn := ft.ElevatedButton(
                        "Buscar Clima",
                        on_click=lambda e: buscar_clima(e),
                        icon=ft.icons.SEARCH,
                        style=ft.ButtonStyle(
                            color=ft.colors.WHITE,
                            bgcolor=COLOR_SECUNDARIO,
                            padding=20
                        )
                    ),
                    loading_indicator := ft.ProgressRing(visible=False, width=20, height=20)
                ], alignment=ft.MainAxisAlignment.CENTER),
            ]),
            padding=30,
            width=500
        )
    )
    
    card_resultado = ft.Card(
        elevation=6,
        visible=False,
        content=ft.Container(
            content=ft.Column([
                resultado_header := ft.Text("", size=22, weight=ft.FontWeight.BOLD),
                ft.Container(height=15),
                ft.Row([
                    ft.Container(
                        content=ft.Column([
                            ft.Text("🌡️", size=30),
                            ft.Text("Temperatura", size=14, color=ft.colors.GREY_600),
                            temp_text := ft.Text("--°C", size=24, weight=ft.FontWeight.BOLD)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        padding=15,
                        width=120,
                        bgcolor=ft.colors.BLUE_50,
                        border_radius=10
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("💧", size=30),
                            ft.Text("Humedad", size=14, color=ft.colors.GREY_600),
                            humedad_text := ft.Text("--%", size=24, weight=ft.FontWeight.BOLD)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        padding=15,
                        width=120,
                        bgcolor=ft.colors.CYAN_50,
                        border_radius=10
                    ),
                    ft.Container(
                        content=ft.Column([
                            ft.Text("💨", size=30),
                            ft.Text("Viento", size=14, color=ft.colors.GREY_600),
                            viento_text := ft.Text("-- km/h", size=24, weight=ft.FontWeight.BOLD)
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        padding=15,
                        width=120,
                        bgcolor=ft.colors.TEAL_50,
                        border_radius=10
                    )
                ], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                ft.Container(height=20),
                ft.Container(
                    content=ft.Column([
                        condicion_text := ft.Text("", size=18, text_align=ft.TextAlign.CENTER),
                        sensacion_text := ft.Text("", size=14, color=ft.colors.GREY_600),
                        presion_text := ft.Text("", size=14, color=ft.colors.GREY_600),
                    ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                    padding=15,
                    bgcolor=ft.colors.GREY_100,
                    border_radius=10,
                    width=400
                ),
                ft.Container(height=10),
                ultima_actualizacion := ft.Text("", size=12, color=ft.colors.GREY_500)
            ]),
            padding=25,
            width=500
        )
    )
    
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
            return
        
        # Mostrar loading
        loading_indicator.visible = True
        buscar_btn.text = "Buscando..."
        page.update()
        
        # Obtener datos reales
        datos_clima = obtener_clima_real(ciudad)
        
        # Ocultar loading
        loading_indicator.visible = False
        buscar_btn.text = "Buscar Clima"
        
        if datos_clima:
            card_resultado.visible = True
            
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
            
            # Actualizar UI
            resultado_header.value = f"{emoji} {datos_clima['ciudad']}, {datos_clima['pais']}"
            temp_text.value = f"{datos_clima['temperatura']}°C"
            humedad_text.value = f"{datos_clima['humedad']}%"
            viento_text.value = f"{datos_clima['viento']} km/h"
            condicion_text.value = f"Condición: {datos_clima['descripcion']}"
            sensacion_text.value = f"Sensación térmica: {datos_clima['sensacion_termica']}°C"
            presion_text.value = f"Presión atmosférica: {datos_clima['presion']} hPa"
            ultima_actualizacion.value = f"🕐 Actualizado: {datetime.now().strftime('%H:%M:%S')}"
        else:
            card_resultado.visible = False
        
        page.update()
    
    # Layout principal
    page.add(
        ft.Column([
            header,
            card_busqueda,
            card_resultado
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0)
    )

if __name__ == "__main__":
    ft.app(target=main)
