from django.shortcuts import render

from productos.models import Producto


# Create your views here.
def inicio(request):
    contexto = {
      'nombre_tienda' : 'Hardware Store',
      'descripcion' : 'Componentes para armar o mejorar tu PC: procesadores, tarjetas de video, '
                      'memorias, almacenamiento y periféricos.',
      'total_productos': Producto.objects.count(),
      'destacados': Producto.objects.exclude(imagen_url='').filter(stock__gt=0).order_by('-precio')[:4],
    }
    return render(request, 'core/inicio.html', contexto)
