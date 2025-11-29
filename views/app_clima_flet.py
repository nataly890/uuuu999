import flet as ft
import requests
import json

def main(page: ft.Page):
    page.title = "Sistema de Clima Global"
    page.padding = 50
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # Componentes
    titulo = ft.Text(" Clima Global", size=35, weight=ft.FontWeight.BOLD)
    
    ciudad_input = ft.TextField(
        label="Ciudad",
        hint_text="Ej: Madrid, Tokyo, New York",
        width=400,
        autofocus=True
    )
    
    resultado_text = ft.Text("", size=18, selectable=True)
    
    def buscar_clima(e):
        ciudad = ciudad_input.value.strip()
        if not ciudad:
            resultado_text.value = " Por favor, ingresa una ciudad"
            page.update()
            return
        
        resultado_text.value = f" Buscando clima para: {ciudad}..."
        page.update()
        
        # Simulación de datos del clima (aquí integrarías una API real)
        datos_simulados = {
            "temperatura": "22°C",
            "descripcion": "Parcialmente nublado",
            "humedad": "65%",
            "viento": "15 km/h"
        }
        
        resultado_text.value = f"""
 Ciudad: {ciudad}
 Temperatura: {datos_simulados['temperatura']}
 Condición: {datos_simulados['descripcion']}
 Humedad: {datos_simulados['humedad']}
 Viento: {datos_simulados['viento']}
        """
        page.update()
    
    buscar_btn = ft.ElevatedButton(
        "Buscar Clima",
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
            ft.Container(height=30),
            ciudad_input,
            ft.Container(height=20),
            buscar_btn,
            ft.Container(height=40),
            resultado_text
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

if __name__ == "__main__":
    ft.app(target=main)
