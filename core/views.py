from django.shortcuts import render

# Create your views here.
def inicio(request):
    contexto = {
      'nombre_tienda' : 'Hardware Store',
      'descripcion' :'Bienvenido a Hardware Store'
    }
    return render(request, 'core/inicio.html', contexto)
