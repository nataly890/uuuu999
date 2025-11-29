import flet as ft
import sqlite3
import random
from datetime import datetime
import os

class ClimaGlobal:
    def __init__(self):
        self.db_path = 'clima_global.db'
        self.init_database()
    
    def init_database(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Tabla de países
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS paises (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                codigo TEXT NOT NULL,
                capital TEXT
            )
        ''')
        
        # Tabla de ciudades
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ciudades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                pais_id INTEGER,
                latitud REAL,
                longitud REAL,
                FOREIGN KEY (pais_id) REFERENCES paises(id)
            )
        ''')
        
        # Tabla de clima histórico
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clima_historico (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ciudad_id INTEGER,
                temperatura REAL,
                humedad INTEGER,
                descripcion TEXT,
                fecha_registro TEXT,
                FOREIGN KEY (ciudad_id) REFERENCES ciudades(id)
            )
        ''')
        
        # Insertar datos de ejemplo si no existen
        cursor.execute('SELECT COUNT(*) FROM paises')
        if cursor.fetchone()[0] == 0:
            self.insertar_datos_ejemplo(cursor)
        
        conn.commit()
        conn.close()
    
    def insertar_datos_ejemplo(self, cursor):
        # Países y ciudades del mundo
        paises = [
            ('Afghanistan', 'AFG', 'Kabul'),
            ('Albania', 'ALB', 'Tirana'),
            ('Argentina', 'ARG', 'Buenos Aires'),
            ('Australia', 'AUS', 'Canberra'),
            ('Brazil', 'BRA', 'Brasilia'),
            ('Canada', 'CAN', 'Ottawa'),
            ('China', 'CHN', 'Beijing'),
            ('France', 'FRA', 'Paris'),
            ('Germany', 'DEU', 'Berlin'),
            ('India', 'IND', 'New Delhi'),
            ('Italy', 'ITA', 'Rome'),
            ('Japan', 'JPN', 'Tokyo'),
            ('Mexico', 'MEX', 'Mexico City'),
            ('Russia', 'RUS', 'Moscow'),
            ('Spain', 'ESP', 'Madrid'),
            ('United Kingdom', 'GBR', 'London'),
            ('United States', 'USA', 'Washington D.C.'),
            ('Egypt', 'EGY', 'Cairo'),
            ('South Africa', 'ZAF', 'Pretoria'),
            ('Chile', 'CHL', 'Santiago')
        ]
        
        cursor.executemany('INSERT INTO paises (nombre, codigo, capital) VALUES (?, ?, ?)', paises)
        
        # Ciudades por país
        ciudades = [
            # Afghanistan
            ('Kabul', 1, 34.5553, 69.2075),
            ('Herat', 1, 34.3411, 62.2030),
            # Albania
            ('Tirana', 2, 41.3275, 19.8187),
            ('Durres', 2, 41.3236, 19.4540),
            # Argentina
            ('Buenos Aires', 3, -34.6037, -58.3816),
            ('Córdoba', 3, -31.4201, -64.1888),
            ('Mendoza', 3, -32.8895, -68.8458),
            # Australia
            ('Sydney', 4, -33.8688, 151.2093),
            ('Melbourne', 4, -37.8136, 144.9631),
            ('Brisbane', 4, -27.4698, 153.0251),
            # Brazil
            ('Rio de Janeiro', 5, -22.9068, -43.1729),
            ('São Paulo', 5, -23.5505, -46.6333),
            ('Brasilia', 5, -15.7975, -47.8919),
            # Canada
            ('Toronto', 6, 43.6532, -79.3832),
            ('Vancouver', 6, 49.2827, -123.1207),
            ('Montreal', 6, 45.5017, -73.5673),
            # China
            ('Beijing', 7, 39.9042, 116.4074),
            ('Shanghai', 7, 31.2304, 121.4737),
            ('Hong Kong', 7, 22.3193, 114.1694),
            # France
            ('Paris', 8, 48.8566, 2.3522),
            ('Lyon', 8, 45.7640, 4.8357),
            ('Marseille', 8, 43.2965, 5.3698),
            # Germany
            ('Berlin', 9, 52.5200, 13.4050),
            ('Munich', 9, 48.1351, 11.5820),
            ('Hamburg', 9, 53.5511, 9.9937),
            # India
            ('Mumbai', 10, 19.0760, 72.8777),
            ('Delhi', 10, 28.6139, 77.2090),
            ('Bangalore', 10, 12.9716, 77.5946),
            # Italy
            ('Rome', 11, 41.9028, 12.4964),
            ('Milan', 11, 45.4642, 9.1900),
            ('Venice', 11, 45.4408, 12.3155),
            # Japan
            ('Tokyo', 12, 35.6762, 139.6503),
            ('Osaka', 12, 34.6937, 135.5023),
            ('Kyoto', 12, 35.0116, 135.7681),
            # Mexico
            ('Mexico City', 13, 19.4326, -99.1332),
            ('Guadalajara', 13, 20.6597, -103.3496),
            ('Monterrey', 13, 25.6866, -100.3161),
            # Russia
            ('Moscow', 14, 55.7558, 37.6173),
            ('Saint Petersburg', 14, 59.9343, 30.3351),
            ('Novosibirsk', 14, 55.0084, 82.9357),
            # Spain
            ('Madrid', 15, 40.4168, -3.7038),
            ('Barcelona', 15, 41.3851, 2.1734),
            ('Valencia', 15, 39.4699, -0.3763),
            # United Kingdom
            ('London', 16, 51.5074, -0.1278),
            ('Manchester', 16, 53.4808, -2.2426),
            ('Edinburgh', 16, 55.9533, -3.1883),
            # United States
            ('New York', 17, 40.7128, -74.0060),
            ('Los Angeles', 17, 34.0522, -118.2437),
            ('Chicago', 17, 41.8781, -87.6298),
            ('Miami', 17, 25.7617, -80.1918),
            # Egypt
            ('Cairo', 18, 30.0444, 31.2357),
            ('Alexandria', 18, 31.2001, 29.9187),
            # South Africa
            ('Johannesburg', 19, -26.2041, 28.0473),
            ('Cape Town', 19, -33.9249, 18.4241),
            # Chile
            ('Santiago', 20, -33.4489, -70.6693),
            ('Valparaíso', 20, -33.0472, -71.6127)
        ]
        
        cursor.executemany('INSERT INTO ciudades (nombre, pais_id, latitud, longitud) VALUES (?, ?, ?, ?)', ciudades)
    
    def obtener_paises(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, nombre FROM paises ORDER BY nombre')
        paises = cursor.fetchall()
        conn.close()
        return paises
    
    def obtener_ciudades_por_pais(self, pais_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('SELECT id, nombre FROM ciudades WHERE pais_id = ? ORDER BY nombre', (pais_id,))
        ciudades = cursor.fetchall()
        conn.close()
        return ciudades
    
    def obtener_clima_real(self, ciudad_id):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('SELECT nombre, latitud, longitud FROM ciudades WHERE id = ?', (ciudad_id,))
            ciudad = cursor.fetchone()
            
            if ciudad:
                nombre_ciudad, lat, lon = ciudad
                
                # Generar clima realista basado en coordenadas
                if lat > 0:  # Hemisferio norte
                    if datetime.now().month in [12, 1, 2]:
                        temp_range = (-10, 15)  # Invierno
                    elif datetime.now().month in [3, 4, 5]:
                        temp_range = (10, 25)   # Primavera
                    elif datetime.now().month in [6, 7, 8]:
                        temp_range = (20, 40)   # Verano
                    else:
                        temp_range = (10, 28)   # Otoño
                else:  # Hemisferio sur
                    if datetime.now().month in [12, 1, 2]:
                        temp_range = (20, 40)   # Verano
                    elif datetime.now().month in [3, 4, 5]:
                        temp_range = (10, 28)   # Otoño
                    elif datetime.now().month in [6, 7, 8]:
                        temp_range = (-10, 15)  # Invierno
                    else:
                        temp_range = (10, 25)   # Primavera
                
                # Ajustar por latitud
                if abs(lat) > 50:  # Regiones polares
                    temp_range = (temp_range[0] - 15, temp_range[1] - 10)
                elif abs(lat) < 23.5:  # Trópicos
                    temp_range = (temp_range[0] + 15, temp_range[1] + 20)
                
                temperatura = random.randint(temp_range[0], temp_range[1])
                condiciones = self._obtener_condicion_clima(temperatura)
                condicion = random.choice(condiciones)
                
                datos_clima = {
                    'ciudad': nombre_ciudad,
                    'temperatura': temperatura,
                    'sensacion_termica': temperatura + random.randint(-5, 5),
                    'humedad': random.randint(20, 95),
                    'presion': random.randint(980, 1040),
                    'viento': round(random.uniform(0, 25), 1),
                    'descripcion': condicion['descripcion'],
                    'icono': condicion['icono'],
                    'latitud': lat,
                    'longitud': lon,
                    'fecha': datetime.now().strftime('%d/%m/%Y %H:%M')
                }
                
                # Guardar en historial
                self._guardar_historial(ciudad_id, datos_clima)
                conn.close()
                return datos_clima
            
            conn.close()
            return None
            
        except Exception as e:
            print(f'Error: {e}')
            return None
    
    def _obtener_condicion_clima(self, temp):
        if temp < 0:
            return [
                {'descripcion': 'Nieve intensa', 'icono': '??'},
                {'descripcion': 'Ventisca', 'icono': '???'},
                {'descripcion': 'Congelante', 'icono': '??'}
            ]
        elif temp < 10:
            return [
                {'descripcion': 'Lluvia intensa', 'icono': '???'},
                {'descripcion': 'Nublado', 'icono': '??'},
                {'descripcion': 'Lluvia ligera', 'icono': '???'}
            ]
        elif temp < 25:
            return [
                {'descripcion': 'Parcialmente nublado', 'icono': '?'},
                {'descripcion': 'Soleado', 'icono': '??'},
                {'descripcion': 'Brisa ligera', 'icono': '??'}
            ]
        else:
            return [
                {'descripcion': 'Soleado', 'icono': '??'},
                {'descripcion': 'Caluroso', 'icono': '??'},
                {'descripcion': 'Despejado', 'icono': '??'}
            ]
    
    def _guardar_historial(self, ciudad_id, datos):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO clima_historico 
            (ciudad_id, temperatura, humedad, descripcion, fecha_registro)
            VALUES (?, ?, ?, ?, ?)
        ''', (ciudad_id, datos['temperatura'], datos['humedad'], datos['descripcion'], datetime.now()))
        conn.commit()
        conn.close()
    
    def obtener_historial(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            SELECT c.nombre, ch.temperatura, ch.descripcion, ch.fecha_registro 
            FROM clima_historico ch
            JOIN ciudades c ON ch.ciudad_id = c.id
            ORDER BY ch.fecha_registro DESC 
            LIMIT 8
        ''')
        historial = cursor.fetchall()
        conn.close()
        return historial

def main(page: ft.Page):
    page.title = 'Clima Global ??'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.ADAPTIVE
    
    app = ClimaGlobal()
    
    # Elementos de la UI
    titulo = ft.Text('?? Clima Global', size=28, weight=ft.FontWeight.BOLD, color=ft.colors.BLUE_900)
    
    # Selector de país
    paises = app.obtener_paises()
    dropdown_pais = ft.Dropdown(
        label='Selecciona un país',
        width=350,
        options=[ft.dropdown.Option(text=pais[1], key=str(pais[0])) for pais in paises]
    )
    
    # Selector de ciudad
    dropdown_ciudad = ft.Dropdown(
        label='Selecciona una ciudad',
        width=350,
        disabled=True
    )
    
    # Botón de búsqueda
    boton_buscar = ft.ElevatedButton(
        '?? Obtener Clima',
        icon=ft.icons.SEARCH,
        disabled=True,
        style=ft.ButtonStyle(padding=20)
    )
    
    # Resultados
    resultado_container = ft.Container(
        padding=25,
        margin=10,
        border_radius=15,
        bgcolor=ft.colors.BLUE_50,
        visible=False,
        width=400
    )
    
    historial_container = ft.Container(
        padding=20,
        margin=10,
        border_radius=15,
        bgcolor=ft.colors.GREY_100,
        visible=False,
        width=400
    )
    
    # Funciones
    def on_pais_change(e):
        if dropdown_pais.value:
            ciudades = app.obtener_ciudades_por_pais(int(dropdown_pais.value))
            dropdown_ciudad.options = [ft.dropdown.Option(text=ciudad[1], key=str(ciudad[0])) for ciudad in ciudades]
            dropdown_ciudad.disabled = False
            boton_buscar.disabled = True
            resultado_container.visible = False
        else:
            dropdown_ciudad.disabled = True
            boton_buscar.disabled = True
        page.update()
    
    def on_ciudad_change(e):
        boton_buscar.disabled = not bool(dropdown_ciudad.value)
        page.update()
    
    def buscar_clima(e):
        if dropdown_ciudad.value:
            # Mostrar loading
            boton_buscar.text = 'Buscando...'
            boton_buscar.disabled = True
            page.update()
            
            datos = app.obtener_clima_real(int(dropdown_ciudad.value))
            
            # Restaurar botón
            boton_buscar.text = '?? Obtener Clima'
            boton_buscar.disabled = False
            
            if datos:
                mostrar_resultado(datos)
                mostrar_historial()
    
    def mostrar_resultado(datos):
        resultado_container.content = ft.Column([
            ft.Text(f'{datos[\"ciudad\"]}', size=24, weight=ft.FontWeight.BOLD),
            ft.Text(f'{datos[\"fecha\"]}', size=12, color=ft.colors.GREY_600),
            ft.Divider(height=10),
            ft.Row([
                ft.Text(f'{datos[\"icono\"]}', size=40),
                ft.Text(f'{datos[\"temperatura\"]}°C', size=36, weight=ft.FontWeight.BOLD),
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.Text(f'{datos[\"descripcion\"]}', size=18, text_align=ft.TextAlign.CENTER),
            ft.Divider(height=20),
            ft.Text(f'?? Sensación térmica: {datos[\"sensacion_termica\"]}°C'),
            ft.Text(f'?? Humedad: {datos[\"humedad\"]}%'),
            ft.Text(f'?? Viento: {datos[\"viento\"]} m/s'),
            ft.Text(f'?? Presión: {datos[\"presion\"]} hPa'),
            ft.Text(f'?? Coordenadas: {datos[\"latitud\"]:.2f}, {datos[\"longitud\"]:.2f}')
        ], spacing=10)
        resultado_container.visible = True
        page.update()
    
    def mostrar_historial():
        historial = app.obtener_historial()
        if historial:
            items = [ft.Text('?? Historial Reciente:', size=16, weight=ft.FontWeight.BOLD)]
            for ciudad, temp, desc, fecha in historial:
                fecha_str = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S.%f').strftime('%d/%m %H:%M')
                items.append(ft.Text(f'• {ciudad}: {temp}°C - {desc} ({fecha_str})', size=12))
            
            historial_container.content = ft.Column(items, spacing=5)
            historial_container.visible = True
            page.update()
    
    # Event handlers
    dropdown_pais.on_change = on_pais_change
    dropdown_ciudad.on_change = on_ciudad_change
    boton_buscar.on_click = buscar_clima
    
    # Layout
    page.add(
        ft.Column([
            titulo,
            ft.Divider(height=30),
            dropdown_pais,
            dropdown_ciudad,
            ft.Row([boton_buscar], alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(height=20),
            resultado_container,
            historial_container
        ], scroll=ft.ScrollMode.ADAPTIVE, spacing=15)
    )

if __name__ == '__main__':
    ft.app(target=main)
