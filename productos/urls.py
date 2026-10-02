from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('<int:id>/editar/', views.editar_producto, name='producto_editar'),
]
