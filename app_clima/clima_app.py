import flet as ft
import random
from datetime import datetime

class ClimaApp:
    def obtener_clima(self, ciudad):
        import time
        time.sleep(1)
        condiciones = [
            {"desc": "Soleado", "icon": "Sol", "temp_range": (20, 35)},
            {"desc": "Parcialmente nublado", "icon": "Nubes", "temp_range": (15, 25)},
            {"desc": "Nublado", "icon": "Nublado", "temp_range": (10, 20)},
            {"desc": "Lluvia ligera", "icon": "Lluvia", "temp_range": (5, 15)}
        ]
        condicion = random.choice(condiciones)
        temp = random.randint(condicion["temp_range"][0], condicion["temp_range"][1])
        return {
            'ciudad': ciudad.title(),
            'pais': "Demo",
            'temperatura': temp,
            'descripcion': condicion["desc"],
            'icono': condicion["icon"],
            'fecha_actual': datetime.now().strftime("%d/%m/%Y %H:%M")
        }

def main(page: ft.Page):
    page.title = "App del Clima"
    page.padding = 20
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    titulo = ft.Text("App del Clima", size=24, weight=ft.FontWeight.BOLD)
    campo_ciudad = ft.TextField(label="Ingresa una ciudad", width=300)
    boton_buscar = ft.ElevatedButton("Buscar Clima")
    resultado_texto = ft.Text()
    
    app = ClimaApp()
    
    def buscar_clima(e):
        ciudad = campo_ciudad.value.strip()
        if ciudad:
            datos = app.obtener_clima(ciudad)
            resultado_texto.value = f"{datos['icono']} {datos['ciudad']}: {datos['temperatura']}°C - {datos['descripcion']}"
            page.update()
    
    boton_buscar.on_click = buscar_clima
    page.add(titulo, campo_ciudad, boton_buscar, resultado_texto)

if __name__ == "__main__":
    ft.app(target=main)
