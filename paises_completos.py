import pycountry

def listar_paises_completos():
    paises = list(pycountry.countries)
    print(f'Total de países: {len(paises)}')
    
    for pais in paises[:20]:  # Mostrar primeros 20
        print(f'{pais.name} ({pais.alpha_2})')

print('=== LISTA COMPLETA DE PAÍSES ===')
listar_paises_completos()
print('\\nUsa pycountry.countries para acceder a todos los países')
