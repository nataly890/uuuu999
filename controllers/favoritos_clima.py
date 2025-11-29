import requests
import json
import os

API_KEY = '04fc66143f78496a9832e01b1804e08a'
FAVORITOS_FILE = 'favoritos_clima.json'

def cargar_favoritos():
    if os.path.exists(FAVORITOS_FILE):
        with open(FAVORITOS_FILE, 'r') as f:
            return json.load(f)
    return []

def guardar_favoritos(favoritos):
    with open(FAVORITOS_FILE, 'w') as f:
        json.dump(favoritos, f)

def menu_favoritos():
    favoritos = cargar_favoritos()
    
    while True:
        print('')
        print('SISTEMA DE CIUDADES FAVORITAS')
        print('==============================')
        print('1. Ver favoritos')
        print('2. Agregar ciudad')
        print('3. Eliminar ciudad')
        print('4. Actualizar clima de favoritos')
        print('5. Salir')
        
        opcion = input('Opcion: ')
        
        if opcion == '1':
            ver_favoritos(favoritos)
        elif opcion == '2':
            agregar_favorito(favoritos)
        elif opcion == '3':
            eliminar_favorito(favoritos)
        elif opcion == '4':
            actualizar_favoritos(favoritos)
        elif opcion == '5':
            break
        else:
            print('Opcion no valida')

def ver_favoritos(favoritos):
    print('')
    print('CIUDADES FAVORITAS:')
    if not favoritos:
        print('No hay ciudades favoritas')
    else:
        for ciudad in favoritos:
            consultar_clima(ciudad)

def agregar_favorito(favoritos):
    ciudad = input('Ciudad a agregar: ')
    if ciudad and ciudad not in favoritos:
        favoritos.append(ciudad)
        guardar_favoritos(favoritos)
        print('Ciudad agregada a favoritos')
    else:
        print('Ciudad ya existe o nombre invalido')

def eliminar_favorito(favoritos):
    if favoritos:
        for i, ciudad in enumerate(favoritos):
            print(f'{i+1}. {ciudad}')
        try:
            idx = int(input('Numero a eliminar: ')) - 1
            if 0 <= idx < len(favoritos):
                ciudad_eliminada = favoritos.pop(idx)
                guardar_favoritos(favoritos)
                print(f'{ciudad_eliminada} eliminada')
        except:
            print('Seleccion invalida')
    else:
        print('No hay ciudades favoritas')

def actualizar_favoritos(favoritos):
    print('')
    print('ACTUALIZANDO FAVORITOS...')
    for ciudad in favoritos:
        consultar_clima(ciudad)

def consultar_clima(ciudad):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=' + ciudad + '&appid=' + API_KEY + '&units=metric&lang=es'
    response = requests.get(url)
    
    if response.status_code == 200:
        datos = response.json()
        print(f'{datos[\"name\"]}: {datos[\"main\"][\"temp\"]:.1f}C - {datos[\"weather\"][0][\"description\"]}')
    else:
        print(f'{ciudad}: No encontrada')

if __name__ == '__main__':
    menu_favoritos()
