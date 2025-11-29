import flet as ft
import random
from datetime import datetime

def main(page):
    # Configuración móvil
    page.title = "Clima Móvil"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Lista de ciudades globales
    ciudades = [
        "Madrid", "Barcelona", "Paris", "London", "Rome",
        "Berlin", "New York", "Los Angeles", "Tokyo", "Sydney", 
        "Mexico City", "Buenos Aires", "Sao Paulo", "Lima", "Bogota",
        "Cairo", "Moscow", "Beijing", "Shanghai", "Mumbai"
    ]
    
    # Elementos de la UI móvil
    titulo = ft.Text("🌍 Clima Mundial", size=28, weight=ft.FontWeight.BOLD)
    
    dropdown_ciudad = ft.Dropdown(
        label="Selecciona ciudad",
        width=350,
        options=[ft.dropdown.Option(ciudad) for ciudad in ciudades]
    )
    
    boton_buscar = ft.ElevatedButton(
        "🔍 Buscar Clima",
        width=350,
        height=50
    )
    
    # Contenedor de resultados
    resultado_card = ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text("Selecciona una ciudad", size=18)
            ]),
            padding=20,
            width=350
        ),
        elevation=5
    )
    
    # Función para buscar clima
    def buscar_clima(e):
        if dropdown_ciudad.value:
            ciudad = dropdown_ciudad.value
            temp = random.randint(-10, 40)
            
            if temp < 0:
                icono = "❄️"
                estado = "Muy frío"
            elif temp < 10:
                icono = "🥶" 
                estado = "Frío"
            elif temp < 20:
                icono = "⛅"
                estado = "Templado"
            elif temp < 30:
                icono = "☀️"
                estado = "Cálido"
            else:
                icono = "🔥"
                estado = "Caluroso"
            
            resultado_card.content.content.controls = [
                ft.Text(f"{icono} {ciudad}", size=22, weight=ft.FontWeight.BOLD),
                ft.Divider(height=10),
                ft.Text(f"{temp}°C", size=36, weight=ft.FontWeight.BOLD),
                ft.Text(estado, size=18),
                ft.Divider(height=15),
                ft.Text(f"💧 Humedad: {random.randint(30, 90)}%"),
                ft.Text(f"🌬 Viento: {random.randint(0, 25)} km/h"),
                ft.Text(f"📅 {datetime.now().strftime('%d/%m/%Y %H:%M')}")
            ]
            
            page.update()
    
    # Conectar evento
    boton_buscar.on_click = buscar_clima
    
    # Diseño móvil
    page.add(
        ft.Column([
            titulo,
            ft.Divider(height=30),
            dropdown_ciudad,
            ft.Divider(height=20),
            boton_buscar,
            ft.Divider(height=30),
            resultado_card
        ], scroll=ft.ScrollMode.ADAPTIVE)
    )

# Ejecutar como app móvil
ft.app(target=main, view=ft.AppView.FLET_APP)
