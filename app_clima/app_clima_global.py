import flet as ft
import requests
import json

class ClimaApp:
    def __init__(self):
        self.api_url = "http://localhost:5000"
    
    def obtener_clima(self, ciudad, pais=""):
        try:
            if pais:
                url = f"{self.api_url}/clima/{ciudad}/{pais}"
            else:
                url = f"{self.api_url}/clima/{ciudad}"
            
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json()
            return None
        except:
            return None
    
    def obtener_continentes(self):
        try:
            response = requests.get(f"{self.api_url}/continentes", timeout=10)
            if response.status_code == 200:
                return response.json()
            return {}
        except:
            return {}
    
    def obtener_ciudades_continente(self, continente):
        try:
            response = requests.get(f"{self.api_url}/ciudades/{continente}", timeout=10)
            if response.status_code == 200:
                return response.json()
            return {}
        except:
            return {}

def main(page: ft.Page):
    page.title = "Clima Global 🌍"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 15
    page.scroll = ft.ScrollMode.ADAPTIVE
    
    app_clima = ClimaApp()
    
    # Header
    header = ft.Container(
        content=ft.Column([
            ft.Text("CLIMA GLOBAL", size=26, weight=ft.FontWeight.BOLD, 
                   color=ft.colors.BLUE_900, text_align=ft.TextAlign.CENTER),
            ft.Text("Datos en tiempo real de todo el mundo", size=14, 
                   color=ft.colors.GREY_700, text_align=ft.TextAlign.CENTER)
        ]),
        padding=20,
        bgcolor=ft.colors.BLUE_50,
        border_radius=15,
        margin=ft.margin.only(bottom=20)
    )
    
    # Panel de continentes
    panel_continentes = ft.Column(scroll=ft.ScrollMode.ADAPTIVE)
    
    # Panel de países
    panel_paises = ft.Column(scroll=ft.ScrollMode.ADAPTIVE)
    
    # Panel de ciudades
    panel_ciudades = ft.Column(scroll=ft.ScrollMode.ADAPTIVE)
    
    # Resultados
    card_resultado = ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text("Selecciona una ciudad", size=16, color=ft.colors.GREY_600)
            ]),
            padding=20,
            width=400
        ),
        elevation=8,
        visible=False
    )
    
    progreso = ft.ProgressRing(visible=False)
    
    # Función para crear botones
    def crear_boton(texto, on_click):
        return ft.TextButton(
            text=texto,
            on_click=on_click,
            style=ft.ButtonStyle(
                padding=15,
                bgcolor=ft.colors.BLUE_50
            )
        )
    
    # Cargar continentes
    def cargar_continentes():
        panel_continentes.controls.clear()
        continentes = app_clima.obtener_continentes()
        
        for continente in continentes.keys():
            panel_continentes.controls.append(
                crear_boton(continente, lambda e, c=continente: cargar_paises(c))
            )
        
        page.update()
    
    # Cargar países del continente
    def cargar_paises(continente):
        panel_paises.controls.clear()
        panel_ciudades.controls.clear()
        card_resultado.visible = False
        
        paises = app_clima.obtener_ciudades_continente(continente)
        
        for pais in paises.keys():
            panel_paises.controls.append(
                crear_boton(pais, lambda e, p=pais, c=continente: cargar_ciudades(p, c))
            )
        
        page.update()
    
    # Cargar ciudades del país
    def cargar_ciudades(pais, continente):
        panel_ciudades.controls.clear()
        card_resultado.visible = False
        
        ciudades_data = app_clima.obtener_ciudades_continente(continente)
        ciudades = ciudades_data.get(pais, [])
        
        for ciudad in ciudades:
            panel_ciudades.controls.append(
                crear_boton(ciudad, lambda e, ci=ciudad, pa=pais: buscar_clima(ci, pa))
            )
        
        page.update()
    
    # Buscar clima
    def buscar_clima(ciudad, pais):
        progreso.visible = True
        card_resultado.visible = False
        page.update()
        
        datos = app_clima.obtener_clima(ciudad, pais)
        progreso.visible = False
        
        if datos:
            mostrar_resultado(datos)
        else:
            mostrar_error()
    
    def mostrar_resultado(datos):
        color_estado = ft.colors.GREEN if datos.get('real', False) else ft.colors.ORANGE
        
        card_resultado.content.content.controls = [
            ft.Row([
                ft.Text(datos['ciudad'], size=22, weight=ft.FontWeight.BOLD),
                ft.Text(datos['pais'], size=14, color=ft.colors.GREY_600)
            ]),
            
            ft.Divider(height=15),
            
            ft.Row([
                ft.Text(f"{datos['temperatura']}°C", size=36, weight=ft.FontWeight.BOLD),
                ft.Column([
                    ft.Text(datos['descripcion'], size=16),
                    ft.Text(f"Sensación: {datos['sensacion_termica']}°C", size=12)
                ])
            ]),
            
            ft.Divider(height=20),
            
            ft.Text("DATOS EN TIEMPO REAL", size=14, weight=ft.FontWeight.BOLD),
            
            ft.Row([
                ft.Column([
                    ft.Text("HUMEDAD", size=11, color=ft.colors.GREY_600),
                    ft.Text(f"{datos['humedad']}%", size=18, weight=ft.FontWeight.BOLD)
                ]),
                
                ft.VerticalDivider(width=20),
                
                ft.Column([
                    ft.Text("VIENTO", size=11, color=ft.colors.GREY_600),
                    ft.Text(f"{datos['viento']} m/s", size=18, weight=ft.FontWeight.BOLD)
                ]),
                
                ft.VerticalDivider(width=20),
                
                ft.Column([
                    ft.Text("PRESIÓN", size=11, color=ft.colors.GREY_600),
                    ft.Text(f"{datos['presion']} hPa", size=14, weight=ft.FontWeight.BOLD)
                ])
            ], alignment=ft.MainAxisAlignment.SPACE_AROUND),
            
            ft.Divider(height=15),
            
            ft.Container(
                content=ft.Row([
                    ft.Text("✓ Datos Reales" if datos.get('real', False) else "⚠ Datos Simulados", 
                           size=12, color=color_estado),
                    ft.Text(f"• {datos['actualizado']}", size=12, color=ft.colors.GREY_600)
                ]),
                padding=5,
                bgcolor=ft.colors.GREY_100,
                border_radius=8
            )
        ]
        
        card_resultado.visible = True
        page.update()
    
    def mostrar_error():
        card_resultado.content.content.controls = [
            ft.Icon(ft.icons.ERROR, size=40, color=ft.colors.RED),
            ft.Text("Error", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.RED),
            ft.Text("No se pudieron obtener los datos", text_align=ft.TextAlign.CENTER)
        ]
        card_resultado.visible = True
        page.update()
    
    # Layout principal
    page.add(
        ft.Column([
            header,
            
            ft.Text("Continentes:", size=16, weight=ft.FontWeight.BOLD),
            panel_continentes,
            
            ft.Divider(height=20),
            
            ft.Text("Países:", size=16, weight=ft.FontWeight.BOLD),
            panel_paises,
            
            ft.Divider(height=20),
            
            ft.Text("Ciudades:", size=16, weight=ft.FontWeight.BOLD),
            panel_ciudades,
            
            ft.Divider(height=20),
            progreso,
            card_resultado
        ], scroll=ft.ScrollMode.ADAPTIVE)
    )
    
    # Cargar datos iniciales
    cargar_continentes()

ft.app(target=main, view=ft.AppView.FLET_APP)
