from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('<int:id>/editar/', views.editar_producto, name='producto_editar'),
    path('<int:id>/eliminar/', views.eliminar_producto, name='producto_eliminar'),
]
