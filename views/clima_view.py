import flet as ft
from controllers.clima_controller import ClimaController

class ClimaView:
    def __init__(self, page):
        self.page = page
        self.controller = ClimaController()
        self._inicializar_ui()
    
    def _inicializar_ui(self):
        self.page.title = "Clima Global MVC"
        self.page.theme_mode = ft.ThemeMode.LIGHT
        self.page.padding = 15
        self.page.scroll = ft.ScrollMode.ADAPTIVE
        
        # Componentes de la UI
        self.header = self._crear_header()
        self.panel_continentes = ft.Column(scroll=ft.ScrollMode.ADAPTIVE)
        self.panel_paises = ft.Column(scroll=ft.ScrollMode.ADAPTIVE)
        self.panel_ciudades = ft.Column(scroll=ft.ScrollMode.ADAPTIVE)
        self.card_resultado = self._crear_card_resultado()
        self.progreso = ft.ProgressRing(visible=False)
        
        # Cargar layout
        self._cargar_layout()
        self._cargar_continentes()
    
    def _crear_header(self):
        return ft.Container(
            content=ft.Column([
                ft.Text("CLIMA GLOBAL MVC", size=26, weight=ft.FontWeight.BOLD, 
                       color=ft.colors.BLUE_900, text_align=ft.TextAlign.CENTER),
                ft.Text("Arquitectura MVC - Datos en Tiempo Real", size=14, 
                       color=ft.colors.GREY_700, text_align=ft.TextAlign.CENTER)
            ]),
            padding=20,
            bgcolor=ft.colors.BLUE_50,
            border_radius=15,
            margin=ft.margin.only(bottom=20)
        )
    
    def _crear_card_resultado(self):
        return ft.Card(
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
    
    def _crear_boton(self, texto, on_click):
        return ft.TextButton(
            text=texto,
            on_click=on_click,
            style=ft.ButtonStyle(
                padding=15,
                bgcolor=ft.colors.BLUE_50
            )
        )
    
    def _cargar_layout(self):
        self.page.add(
            ft.Column([
                self.header,
                
                ft.Text("Continentes:", size=16, weight=ft.FontWeight.BOLD),
                self.panel_continentes,
                
                ft.Divider(height=20),
                
                ft.Text("Países:", size=16, weight=ft.FontWeight.BOLD),
                self.panel_paises,
                
                ft.Divider(height=20),
                
                ft.Text("Ciudades:", size=16, weight=ft.FontWeight.BOLD),
                self.panel_ciudades,
                
                ft.Divider(height=20),
                self.progreso,
                self.card_resultado
            ], scroll=ft.ScrollMode.ADAPTIVE)
        )
    
    def _cargar_continentes(self):
        self.panel_continentes.controls.clear()
        continentes = self.controller.obtener_continentes()
        
        for continente in continentes:
            self.panel_continentes.controls.append(
                self._crear_boton(continente, lambda e, c=continente: self._cargar_paises(c))
            )
        
        self.page.update()
    
    def _cargar_paises(self, continente):
        self.panel_paises.controls.clear()
        self.panel_ciudades.controls.clear()
        self.card_resultado.visible = False
        
        paises = self.controller.obtener_paises(continente)
        
        for pais in paises:
            self.panel_paises.controls.append(
                self._crear_boton(pais, lambda e, p=pais, c=continente: self._cargar_ciudades(p, c))
            )
        
        self.page.update()
    
    def _cargar_ciudades(self, pais, continente):
        self.panel_ciudades.controls.clear()
        self.card_resultado.visible = False
        
        ciudades = self.controller.obtener_ciudades(continente, pais)
        
        for ciudad in ciudades:
            self.panel_ciudades.controls.append(
                self._crear_boton(ciudad, lambda e, ci=ciudad, pa=pais: self._buscar_clima(ci, pa))
            )
        
        self.page.update()
    
    def _buscar_clima(self, ciudad, pais):
        self.progreso.visible = True
        self.card_resultado.visible = False
        self.page.update()
        
        datos = self.controller.obtener_clima_ciudad(ciudad, pais)
        self.progreso.visible = False
        
        if datos:
            self._mostrar_resultado(datos)
        else:
            self._mostrar_error()
    
    def _mostrar_resultado(self, datos):
        color_estado = ft.colors.GREEN if datos.get('real', False) else ft.colors.ORANGE
        
        self.card_resultado.content.content.controls = [
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
        
        self.card_resultado.visible = True
        self.page.update()
    
    def _mostrar_error(self):
        self.card_resultado.content.content.controls = [
            ft.Icon(ft.icons.ERROR, size=40, color=ft.colors.RED),
            ft.Text("Error", size=18, weight=ft.FontWeight.BOLD, color=ft.colors.RED),
            ft.Text("No se pudieron obtener los datos", text_align=ft.TextAlign.CENTER)
        ]
        self.card_resultado.visible = True
        self.page.update()
