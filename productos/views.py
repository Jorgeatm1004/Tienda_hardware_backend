from django.shortcuts import render
from .models import Producto


def catalogo(request):
    # Consulta a la base de datos con el ORM, ordenada por nombre
    productos = Producto.objects.all().order_by('nombre')
    contexto = {
        'titulo': 'Catálogo de Productos',
        'productos': productos,
        'cantidad_productos': productos.count(),
    }
    return render(request, 'productos/catalogo.html', contexto)
