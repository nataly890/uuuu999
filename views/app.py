import flet as ft
from views.clima_view import ClimaView

def main(page: ft.Page):
    # Inicializar la vista
    clima_view = ClimaView(page)

# Ejecutar la aplicación
if __name__ == '__main__':
    ft.app(target=main, view=ft.AppView.FLET_APP)
