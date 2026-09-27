from django.shortcuts import render

# Create your views here.
def pedidos(request):
    pedido_ejemplo = {
        'id_despacho': 'DSP001',
        'cliente': 'Juan Perez',
        'fecha_compra': '10-09-2026',
        'estado_despacho': 'En tránsito',
        'productos': [
            {'nombre': 'Procesador Ryzen 5 5600X', 'cantidad': 1 },
            {'nombre': 'Tarjeta de video NVIDIA GeForce RTX 3060', 'cantidad': 1 },
            {'nombre': 'Memoria RAM Corsair Vengeance 16GB', 'cantidad': 2 },
        ],
        'fecha_entrega': '20-09-2026',
        
    }
    contexto = {
        'titulo': 'Seguimiento de pedidos',
        'pedido': pedido_ejemplo,
    }
    return render(request, 'pedidos/pedidos.html', contexto)