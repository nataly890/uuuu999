import flet as ft
import random

def main(page):
    page.title = "App Clima Flet"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Crear elementos
    titulo = ft.Text("🌤️ App del Clima", size=30, weight=ft.FontWeight.BOLD)
    
    campo_ciudad = ft.TextField(
        label="Nombre de la ciudad",
        width=300,
        hint_text="Ej: Madrid, Tokyo, New York"
    )
    
    boton = ft.ElevatedButton("Obtener Clima")
    
    resultado = ft.Text("", size=20, color=ft.colors.BLUE)
    
    # Función para obtener clima
    def obtener_clima(e):
        ciudad = campo_ciudad.value
        if ciudad:
            temperatura = random.randint(-5, 35)
            condiciones = ["Soleado", "Nublado", "Lluvioso", "Ventoso"]
            condicion = random.choice(condiciones)
            
            resultado.value = f"{ciudad}: {temperatura}°C - {condicion}"
            resultado.color = ft.colors.GREEN
        else:
            resultado.value = "Por favor, ingresa una ciudad"
            resultado.color = ft.colors.RED
        
        page.update()
    
    # Conectar el botón
    boton.on_click = obtener_clima
    
    # Agregar elementos a la página
    page.add(
        titulo,
        ft.Divider(height=20),
        campo_ciudad,
        ft.Divider(height=10),
        boton,
        ft.Divider(height=20),
        resultado
    )

ft.app(target=main)
