import flet as ft
import requests
from datetime import datetime

class ClimaGlobalReal:
    def __init__(self):
        self.api_key = "8c78ac9a4d4a9db0f7862c5696560f7a"
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def obtener_clima_real(self, ciudad, pais=""):
        try:
            query = f"{ciudad},{pais}" if pais else ciudad
            params = {
                'q': query,
                'appid': self.api_key,
                'units': 'metric',
                'lang': 'es'
            }
            
            response = requests.get(self.base_url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                return self._procesar_datos_reales(data)
            else:
                return self._datos_simulados(ciudad, pais)
                
        except Exception as e:
            print(f"Error API: {e}")
            return self._datos_simulados(ciudad, pais)
    
    def _procesar_datos_reales(self, data):
        icon_map = {
            '01d': '☀️', '01n': '🌙', '02d': '⛅', '02n': '⛅',
            '03d': '☁️', '03n': '☁️', '04d': '☁️', '04n': '☁️',
            '09d': '🌧️', '09n': '🌧️', '10d': '🌦️', '10n': '🌦️',
            '11d': '⛈️', '11n': '⛈️', '13d': '❄️', '13n': '❄️',
            '50d': '🌫️', '50n': '🌫️'
        }
        
        icon_code = data['weather'][0]['icon']
        icono = icon_map.get(icon_code, '🌍')
        
        return {
            'ciudad': data['name'],
            'pais': data['sys']['country'],
            'temperatura': round(data['main']['temp']),
            'sensacion_termica': round(data['main']['feels_like']),
            'humedad': data['main']['humidity'],
            'presion': data['main']['pressure'],
            'viento': round(data['wind']['speed'], 1),
            'descripcion': data['weather'][0]['description'].title(),
            'icono': icono,
            'actualizado': datetime.now().strftime('%H:%M:%S'),
            'real': True
        }
    
    def _datos_simulados(self, ciudad, pais):
        import random
        temp = random.randint(-5, 35)
        
        if temp < 0:
            icono, desc = "❄️", "Muy frío"
        elif temp < 10:
            icono, desc = "🥶", "Frío"
        elif temp < 20:
            icono, desc = "⛅", "Templado"
        elif temp < 30:
            icono, desc = "☀️", "Cálido"
        else:
            icono, desc = "🔥", "Caluroso"
        
        return {
            'ciudad': ciudad,
            'pais': pais,
            'temperatura': temp,
            'sensacion_termica': temp + random.randint(-3, 2),
            'humedad': random.randint(30, 90),
            'presion': random.randint(980, 1030),
            'viento': round(random.uniform(0, 15), 1),
            'descripcion': desc,
            'icono': icono,
            'actualizado': datetime.now().strftime('%H:%M:%S') + " (SIM)",
            'real': False
        }

# Base de datos completa por continentes
CONTINENTES = {
    "🌍 Europa": {
        "🇪🇸 España": ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao", "Málaga", "Zaragoza"],
        "🇫🇷 Francia": ["Paris", "Lyon", "Marsella", "Toulouse", "Niza", "Bordeaux", "Lille"],
        "🇮🇹 Italia": ["Rome", "Milan", "Naples", "Turin", "Florence", "Venice", "Bologna"],
        "🇩🇪 Alemania": ["Berlin", "Munich", "Hamburg", "Frankfurt", "Cologne", "Stuttgart", "Düsseldorf"],
        "🇬🇧 Reino Unido": ["London", "Manchester", "Birmingham", "Glasgow", "Liverpool", "Edinburgh", "Leeds"],
        "🇵🇹 Portugal": ["Lisbon", "Porto", "Braga", "Coimbra", "Faro", "Aveiro", "Setubal"],
        "🇳🇱 Países Bajos": ["Amsterdam", "Rotterdam", "The Hague", "Utrecht", "Eindhoven", "Groningen", "Tilburg"]
    },
    "🌎 América del Norte": {
        "🇺🇸 Estados Unidos": ["New York", "Los Angeles", "Chicago", "Miami", "Houston", "Phoenix", "Philadelphia"],
        "🇨🇦 Canadá": ["Toronto", "Vancouver", "Montreal", "Calgary", "Ottawa", "Edmonton", "Winnipeg"],
        "🇲🇽 México": ["Mexico City", "Guadalajara", "Monterrey", "Puebla", "Tijuana", "León", "Zapopan"]
    },
    "🌎 América del Sur": {
        "🇦🇷 Argentina": ["Buenos Aires", "Cordoba", "Rosario", "Mendoza", "La Plata", "Mar del Plata", "Salta"],
        "🇧🇷 Brasil": ["Sao Paulo", "Rio de Janeiro", "Brasilia", "Salvador", "Fortaleza", "Belo Horizonte", "Manaus"],
        "🇨🇱 Chile": ["Santiago", "Valparaiso", "Concepcion", "La Serena", "Antofagasta", "Temuco", "Rancagua"],
        "🇨🇴 Colombia": ["Bogota", "Medellin", "Cali", "Barranquilla", "Cartagena", "Cucuta", "Bucaramanga"],
        "🇵🇪 Perú": ["Lima", "Arequipa", "Trujillo", "Chiclayo", "Piura", "Iquitos", "Cusco"],
        "🇻🇪 Venezuela": ["Caracas", "Maracaibo", "Valencia", "Barquisimeto", "Maracay", "Ciudad Guayana", "Maturin"]
    },
    "🌏 Asia": {
        "🇨🇳 China": ["Beijing", "Shanghai", "Guangzhou", "Shenzhen", "Chengdu", "Wuhan", "Xi'an"],
        "🇯🇵 Japón": ["Tokyo", "Osaka", "Kyoto", "Yokohama", "Nagoya", "Sapporo", "Fukuoka"],
        "🇮🇳 India": ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Ahmedabad", "Chennai", "Kolkata"],
        "🇰🇷 Corea del Sur": ["Seoul", "Busan", "Incheon", "Daegu", "Daejeon", "Gwangju", "Ulsan"],
        "🇹🇭 Tailandia": ["Bangkok", "Chiang Mai", "Phuket", "Pattaya", "Khon Kaen", "Udon Thani", "Hat Yai"],
        "🇸🇬 Singapur": ["Singapore"],
        "🇲🇾 Malasia": ["Kuala Lumpur", "Penang", "Johor Bahru", "Ipoh", "Kuching", "Kota Kinabalu"]
    },
    "🌍 África": {
        "🇪🇬 Egipto": ["Cairo", "Alexandria", "Giza", "Shubra El Kheima", "Port Said", "Suez", "Luxor"],
        "🇳🇬 Nigeria": ["Lagos", "Kano", "Ibadan", "Kaduna", "Port Harcourt", "Benin City", "Maiduguri"],
        "🇿🇦 Sudáfrica": ["Johannesburg", "Cape Town", "Durban", "Pretoria", "Port Elizabeth", "Bloemfontein", "East London"],
        "🇰🇪 Kenia": ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Malindi", "Thika"],
        "🇲🇦 Marruecos": ["Casablanca", "Rabat", "Fes", "Marrakech", "Tangier", "Agadir", "Meknes"],
        "🇩🇿 Argelia": ["Algiers", "Oran", "Constantine", "Annaba", "Blida", "Batna", "Djelfa"]
    },
    "🌏 Oceanía": {
        "🇦🇺 Australia": ["Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", "Gold Coast", "Canberra"],
        "🇳🇿 Nueva Zelanda": ["Auckland", "Wellington", "Christchurch", "Hamilton", "Tauranga", "Dunedin", "Palmerston North"],
        "🇫🇯 Fiji": ["Suva", "Lautoka", "Nadi", "Labasa", "Ba", "Levuka", "Sigatoka"],
        "🇵🇬 Papúa Nueva Guinea": ["Port Moresby", "Lae", "Arawa", "Mount Hagen", "Popondetta", "Madang", "Kokopo"]
    }
}

def main(page: ft.Page):
    page.title = "🌤️ Clima Global por Continentes"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 10
    page.scroll = ft.ScrollMode.ADAPTIVE
    
    app_clima = ClimaGlobalReal()
    ciudad_actual = None
    
    # Header
    header = ft.Container(
        content=ft.Column([
            ft.Text("🌍 CLIMA GLOBAL", size=26, weight=ft.FontWeight.BOLD, 
                   color=ft.colors.BLUE_900, text_align=ft.TextAlign.CENTER),
            ft.Text("Datos en Tiempo Real por Continente", size=14, 
                   color=ft.colors.GREY_700, text_align=ft.TextAlign.CENTER)
        ]),
        padding=15,
        bgcolor=ft.colors.BLUE_50,
        border_radius=10,
        margin=ft.margin.only(bottom=10)
    )
    
    # Panel de selección de continentes
    panel_continentes = ft.Column(scroll=ft.ScrollMode.ADAPTIVE)
    
    # Panel de resultados
    panel_resultado = ft.Card(
        content=ft.Container(
            content=ft.Column([
                ft.Text("Selecciona una ciudad", size=18, color=ft.colors.GREY_600,
                       text_align=ft.TextAlign.CENTER)
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            padding=20,
            width=400
        ),
        elevation=8,
        margin=10,
        visible=False
    )
    
    # Progreso
    progreso = ft.ProgressRing(visible=False)
    
    # Función para crear botones de ciudad
    def crear_boton_ciudad(ciudad, pais):
        return ft.TextButton(
            content=ft.Container(
                content=ft.Row([
                    ft.Text(ciudad, size=14, weight=ft.FontWeight.W500),
                    ft.Icon(ft.icons.ARROW_FORWARD_IOS, size=14, color=ft.colors.BLUE)
                ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                padding=10
            ),
            on_click=lambda e, c=ciudad, p=pais: buscar_ciudad(c, p),
            style=ft.ButtonStyle(
                bgcolor=ft.colors.BLUE_50,
                shape=ft.RoundedRectangleBorder(radius=8)
            )
        )
    
    # Función para mostrar continente
    def mostrar_continente(continente_nombre):
        panel_continentes.controls.clear()
        
        for pais, ciudades in CONTINENTES[continente_nombre].items():
            # Header del país
            panel_continentes.controls.append(
                ft.Container(
                    content=ft.Text(pais, size=16, weight=ft.FontWeight.BOLD,
                                  color=ft.colors.BLUE_800),
                    padding=ft.padding.only(top=15, bottom=5, left=10)
                )
            )
            
            # Botones de ciudades
            for ciudad in ciudades:
                panel_continentes.controls.append(
                    crear_boton_ciudad(ciudad, pais.split(" ")[-1])
                )
        
        page.update()
    
    # Función para buscar clima
    def buscar_ciudad(ciudad, pais):
        nonlocal ciudad_actual
        ciudad_actual = f"{ciudad}, {pais}"
        
        # Mostrar progreso
        progreso.visible = True
        panel_resultado.visible = False
        page.update()
        
        # Obtener datos
        datos = app_clima.obtener_clima_real(ciudad, pais)
        
        # Ocultar progreso
        progreso.visible = False
        
        if datos:
            mostrar_resultado(datos)
        else:
            mostrar_error("No se pudieron obtener los datos")
    
    def mostrar_resultado(datos):
        color_estado = ft.colors.GREEN if datos['real'] else ft.colors.ORANGE
        
        panel_resultado.content.content.controls = [
            # Header
            ft.Row([
                ft.Text(datos['icono'], size=28),
                ft.Column([
                    ft.Text(datos['ciudad'], size=20, weight=ft.FontWeight.BOLD),
                    ft.Text(datos['pais'], size=14, color=ft.colors.GREY_600)
                ])
            ], alignment=ft.MainAxisAlignment.CENTER),
            
            ft.Divider(height=15),
            
            # Temperatura principal
            ft.Row([
                ft.Text(f"{datos['temperatura']}°", size=42, weight=ft.FontWeight.BOLD),
                ft.Column([
                    ft.Text(datos['descripcion'], size=16),
                    ft.Text(f"Sensación: {datos['sensacion_termica']}°C", size=12)
                ])
            ], alignment=ft.MainAxisAlignment.SPACE_AROUND),
            
            ft.Divider(height=20),
            
            # Datos principales en tiempo real
            ft.Text("📊 DATOS EN TIEMPO REAL", size=14, weight=ft.FontWeight.BOLD,
                  color=ft.colors.BLUE_700),
            
            ft.Row([
                ft.Column([
                    ft.Text("💧 HUMEDAD", size=11, color=ft.colors.GREY_600),
                    ft.Text(f"{datos['humedad']}%", size=18, weight=ft.FontWeight.BOLD)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                
                ft.VerticalDivider(width=20),
                
                ft.Column([
                    ft.Text("🌬 VIENTO", size=11, color=ft.colors.GREY_600),
                    ft.Text(f"{datos['viento']} m/s", size=18, weight=ft.FontWeight.BOLD)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                
                ft.VerticalDivider(width=20),
                
                ft.Column([
                    ft.Text("📊 PRESIÓN", size=11, color=ft.colors.GREY_600),
                    ft.Text(f"{datos['presion']} hPa", size=16, weight=ft.FontWeight.BOLD)
                ], horizontal_alignment=ft.CrossAxisAlignment.CENTER)
            ], alignment=ft.MainAxisAlignment.SPACE_AROUND),
            
            ft.Divider(height=15),
            
            # Estado de los datos
            ft.Container(
                content=ft.Row([
                    ft.Icon(ft.icons.CHECK_CIRCLE if datos['real'] else ft.icons.WARNING,
                           color=color_estado, size=16),
                    ft.Text("Datos Reales" if datos['real'] else "Datos Simulados", 
                           size=12, color=color_estado),
                    ft.Text(f"• Actualizado: {datos['actualizado']}", 
                           size=12, color=ft.colors.GREY_600)
                ]),
                padding=5,
                bgcolor=ft.colors.GREY_100,
                border_radius=8
            )
        ]
        
        panel_resultado.visible = True
        page.update()
    
    def mostrar_error(mensaje):
        panel_resultado.content.content.controls = [
            ft.Icon(ft.icons.ERROR, size=40, color=ft.colors.RED),
            ft.Text("Error", size=18, color=ft.colors.RED, weight=ft.FontWeight.BOLD),
            ft.Text(mensaje, text_align=ft.TextAlign.CENTER)
        ]
        panel_resultado.visible = True
        page.update()
    
    # Crear botones de continentes
    botones_continentes = ft.Row(scroll=ft.ScrollMode.ADAPTIVE)
    for continente in CONTINENTES.keys():
        boton = ft.ElevatedButton(
            content=ft.Text(continente, size=14),
            on_click=lambda e, c=continente: mostrar_continente(c),
            style=ft.ButtonStyle(
                padding=15,
                bgcolor=ft.colors.BLUE_100
            )
        )
        botones_continentes.controls.append(boton)
    
    # Layout principal
    page.add(
        ft.Column([
            header,
            
            ft.Text("Selecciona un continente:", size=16, weight=ft.FontWeight.BOLD),
            ft.Container(
                content=botones_continentes,
                padding=10
            ),
            
            ft.Divider(height=20),
            
            ft.Text("Ciudades disponibles:", size=16, weight=ft.FontWeight.BOLD),
            panel_continentes,
            
            ft.Divider(height=20),
            progreso,
            panel_resultado
        ], scroll=ft.ScrollMode.ADAPTIVE)
    )
    
    # Mostrar Europa por defecto
    mostrar_continente("🌍 Europa")

ft.app(target=main, view=ft.AppView.FLET_APP)
