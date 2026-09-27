from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista, name='usuarios_lista'),
    path('<int:id>/', views.detalle, name='usuarios_detalle'),
]
