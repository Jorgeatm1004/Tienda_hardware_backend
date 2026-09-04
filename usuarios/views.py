from django.shortcuts import render

# Vendedores de la tienda. Datos de ejemplo en memoria: todavia no hay
# base de datos (eso entra en una evaluacion posterior).
VENDEDORES = [
    {
        'id': 1,
        'nombre': 'Ferretronic',
        'rol': 'Tienda oficial',
        'ciudad': 'Santiago',
        'activo': True,
        'publicaciones': 42,
        'descripcion': 'Distribuidor de componentes para PC de escritorio y gaming.',
    },
    {
        'id': 2,
        'nombre': 'Nodo Norte',
        'rol': 'Vendedor',
        'ciudad': 'Antofagasta',
        'activo': True,
        'publicaciones': 18,
        'descripcion': 'Placas madre, memorias RAM y almacenamiento SSD.',
    },
    {
        'id': 3,
        'nombre': 'GPU Chile',
        'rol': 'Tienda oficial',
        'ciudad': 'Valparaiso',
        'activo': True,
        'publicaciones': 27,
        'descripcion': 'Especialistas en tarjetas graficas y refrigeracion liquida.',
    },
    {
        'id': 4,
        'nombre': 'RetroBits',
        'rol': 'Vendedor',
        'ciudad': 'Concepcion',
        'activo': False,
        'publicaciones': 5,
        'descripcion': 'Repuestos y piezas de segunda mano. Cuenta en pausa.',
    },
]


def lista(request):
    contexto = {
        'vendedores': VENDEDORES,
        'total': len(VENDEDORES),
    }
    return render(request, 'usuarios/lista.html', contexto)


def detalle(request, id):
    vendedor = None
    for v in VENDEDORES:
        if v['id'] == id:
            vendedor = v
            break
    return render(request, 'usuarios/detalle.html', {'vendedor': vendedor})
