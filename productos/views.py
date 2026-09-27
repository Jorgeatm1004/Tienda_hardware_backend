from django.shortcuts import render

# Create your views here.
def catalogo(request):
    lista_productos = [
        {'nombre': 'Procesador Ryzen 5 5600X', 'precio': 150000, 'stock': 10},
        {'nombre': 'Tarjeta de video NVIDIA RTX 3060 12GB', 'precio': 350000, 'stock': 5},
        {'nombre': 'Memoria RAM Corsair Vengeance 16GB DDR4', 'precio': 120000, 'stock': 20},
        {'nombre': 'SSD NVMe 1TB', 'precio': 200000, 'stock': 15},
        {'nombre': 'Motherboard MSI B550 Tomahawk', 'precio': 232000, 'stock': 5},
        {'nombre': 'Fuente de poder EVGA 650W', 'precio': 100000, 'stock': 8},
        {'nombre': 'Gabinete NZXT H510', 'precio': 90000, 'stock': 12},
        {'nombre': 'Monitor LG UltraGear 27" 144Hz', 'precio': 250000, 'stock': 7},
        {'nombre': 'Teclado mecánico Razer BlackWidow', 'precio': 80000, 'stock': 10},
        {'nombre': 'Mouse Logitech G502 HERO', 'precio': 60000, 'stock': 15},
    ]
    contexto = {
        'titulo': 'Catálogo de Productos',
        'productos': lista_productos,
        'cantidad_productos': len(lista_productos)
    }
    return render(request, 'productos/catalogo.html', contexto)
