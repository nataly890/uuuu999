import flet as ft
from datetime import datetime
from ..controllers.clima_controller import ClimaController

class VistaPrincipal:
    def __init__(self):
        self.controller = ClimaController()
        self.color_primario = ft.colors.BLUE_900
        self.color_secundario = ft.colors.CYAN_700
    
    def crear_vista(self, page):
        page.title = \"🌍 Clima Global Pro - MVC\"
        page.padding = 30
        page.theme_mode = ft.ThemeMode.LIGHT
        page.bgcolor = ft.colors.BLUE_GREY_50
        
        # Header
        header = self._crear_header()
        
        # Card de búsqueda
        self.ciudad_input = ft.TextField(
            label=\"Nombre de la ciudad\",
            hint_text=\"Ej: Madrid, Tokyo, New York...\",
            width=400,
            autofocus=True,
            border_color=self.color_primario,
            prefix_icon=ft.icons.LOCATION_ON
        )
        
        self.loading_indicator = ft.ProgressRing(visible=False, width=20, height=20)
        self.buscar_btn = ft.ElevatedButton(
            \"Buscar Clima\",
            on_click=lambda e: self._buscar_clima(page),
            icon=ft.icons.SEARCH,
            style=ft.ButtonStyle(
                color=ft.colors.WHITE,
                bgcolor=self.color_secundario,
                padding=20
            )
        )
        
        # Card de resultados
        self.card_resultado = self._crear_card_resultado()
        
        # Layout principal
        page.add(
            ft.Column([
                header,
                self._crear_card_busqueda(),
                self.card_resultado
            ], alignment=ft.MainAxisAlignment.START, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
        )
    
    def _crear_header(self):
        return ft.Container(
            content=ft.Column([
                ft.Text(\"🌤️\", size=50),
                ft.Text(\"CLIMA GLOBAL PRO - MVC\", size=28, weight=ft.FontWeight.BOLD, color=self.color_primario),
                ft.Text(\"Arquitectura Modelo-Vista-Controlador\", size=16, color=ft.colors.GREY_600),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            margin=ft.margin.only(bottom=20)
        )
    
    def _crear_card_busqueda(self):
        return ft.Card(
            elevation=8,
            content=ft.Container(
                content=ft.Column([
                    ft.Text(\"🔍 Buscar Ciudad\", size=20, weight=ft.FontWeight.BOLD, color=self.color_primario),
                    ft.Container(height=10),
                    self.ciudad_input,
                    ft.Container(height=15),
                    ft.Row([self.buscar_btn, self.loading_indicator], alignment=ft.MainAxisAlignment.CENTER),
                ]),
                padding=30,
                width=500
            )
        )
    
    def _crear_card_resultado(self):
        return ft.Card(
            elevation=6,
            visible=False,
            content=ft.Container(
                content=ft.Column([
                    self.resultado_header := ft.Text(\"\", size=22, weight=ft.FontWeight.BOLD),
                    ft.Container(height=15),
                    ft.Row([
                        self._crear_metric_card(\"🌡️\", \"Temperatura\", \"--°C\", ft.colors.BLUE_50),
                        self._crear_metric_card(\"💧\", \"Humedad\", \"--%\", ft.colors.CYAN_50),
                        self._crear_metric_card(\"💨\", \"Viento\", \"-- km/h\", ft.colors.TEAL_50)
                    ], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                    ft.Container(height=20),
                    ft.Container(
                        content=ft.Column([
                            self.condicion_text := ft.Text(\"\", size=18, text_align=ft.TextAlign.CENTER),
                            self.actualizacion_text := ft.Text(\"\", size=12, color=ft.colors.GREY_500),
                        ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                        padding=15,
                        bgcolor=ft.colors.GREY_100,
                        border_radius=10,
                        width=400
                    ),
                ]),
                padding=25,
                width=500
            )
        )
    
    def _crear_metric_card(self, emoji, titulo, valor, color):
        return ft.Container(
            content=ft.Column([
                ft.Text(emoji, size=30),
                ft.Text(titulo, size=14, color=ft.colors.GREY_600),
                ft.Text(valor, size=24, weight=ft.FontWeight.BOLD)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=15,
            width=120,
            bgcolor=color,
            border_radius=10
        )
    
    def _buscar_clima(self, page):
        ciudad = self.ciudad_input.value
        if not ciudad:
            return
        
        # Mostrar loading
        self.loading_indicator.visible = True
        self.buscar_btn.text = \"Buscando...\"
        page.update()
        
        # Usar controller para buscar clima
        datos_clima = self.controller.buscar_clima(ciudad)
        datos_formateados = self.controller.formatear_datos_clima(datos_clima)
        
        # Ocultar loading
        self.loading_indicator.visible = False
        self.buscar_btn.text = \"Buscar Clima\"
        
        if datos_formateados:
            self.card_resultado.visible = True
            self.resultado_header.value = datos_formateados['header']
            # Actualizar métricas...
            self.condicion_text.value = f\"Condición: {datos_formateados['descripcion']}\"
            self.actualizacion_text.value = f\"🕐 Actualizado: {datos_formateados['fecha_actualizacion']}\"
        else:
            self.card_resultado.visible = False
        
        page.update()

def main(page: ft.Page):
    vista = VistaPrincipal()
    vista.crear_vista(page)

if __name__ == \"__main__\":
    ft.app(target=main)
