from django.shortcuts import render

def pedidos(request):
    lista_pedidos = [
        {
            'id_despacho': 'DSP001',
            'cliente': 'Juan Perez',
            'fecha_compra': '10-09-2026',
            'estado_despacho': 'En tránsito',
            'productos': [
                {'nombre': 'Procesador Ryzen 5 5600X', 'cantidad': 1},
                {'nombre': 'Tarjeta de video NVIDIA GeForce RTX 3060', 'cantidad': 1},
                {'nombre': 'Memoria RAM Corsair Vengeance 16GB', 'cantidad': 2},
            ],
            'fecha_entrega': '20-09-2026',
            'direccion_entrega': 'Calle 123, Puerto Montt',
        },
        {
            'id_despacho': 'DSP002',
            'cliente': 'María González',
            'fecha_compra': '08-09-2026',
            'estado_despacho': 'Entregado',
            'productos': [
                {'nombre': 'SSD NVMe 1TB', 'cantidad': 1},
            ],
            'fecha_entrega': '12-09-2026',
            'direccion_entrega': 'Av. Siempre Viva 742',
        },
    ]

    contexto = {
        'titulo': 'Seguimiento de pedidos',
        'pedidos': lista_pedidos,
    }
    return render(request, 'pedidos/pedidos.html', contexto)