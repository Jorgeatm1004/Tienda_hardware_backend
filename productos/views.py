from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProductoForm
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


def editar_producto(request, id):
    # Si el id no existe se responde 404 en vez de un error 500
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('catalogo')
    else:
        form = ProductoForm(instance=producto)
    contexto = {
        'titulo': f'Editar: {producto.nombre}',
        'form': form,
        'producto': producto,
    }
    return render(request, 'productos/editar.html', contexto)


def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    # GET muestra la confirmación; solo un POST (con CSRF) borra el registro
    if request.method == 'POST':
        producto.delete()
        return redirect('catalogo')
    contexto = {
        'titulo': 'Eliminar producto',
        'producto': producto,
    }
    return render(request, 'productos/eliminar.html', contexto)
