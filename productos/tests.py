from django.test import TestCase
from django.urls import reverse

from .forms import ProductoForm
from .models import Producto


class CatalogoTests(TestCase):
    def test_catalogo_vacio(self):
        respuesta = self.client.get(reverse('catalogo'))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'No hay productos registrados')

    def test_catalogo_lista_productos_desde_bd(self):
        Producto.objects.create(nombre='SSD NVMe 1TB', descripcion='x', precio=200000, stock=15)
        Producto.objects.create(nombre='Gabinete NZXT H510', descripcion='x', precio=90000, stock=0)
        respuesta = self.client.get(reverse('catalogo'))
        self.assertContains(respuesta, 'SSD NVMe 1TB')
        self.assertContains(respuesta, 'Agotado')
        self.assertEqual(respuesta.context['cantidad_productos'], 2)
        # ordenado por nombre
        nombres = [p.nombre for p in respuesta.context['productos']]
        self.assertEqual(nombres, ['Gabinete NZXT H510', 'SSD NVMe 1TB'])


class ProductoFormTests(TestCase):
    def test_form_valido(self):
        form = ProductoForm(data={'nombre': 'Mouse', 'descripcion': 'Mouse gamer', 'precio': 60000, 'stock': 3})
        self.assertTrue(form.is_valid())

    def test_form_sin_nombre_es_invalido(self):
        form = ProductoForm(data={'nombre': '', 'descripcion': 'x', 'precio': 1000, 'stock': 1})
        self.assertFalse(form.is_valid())
        self.assertIn('nombre', form.errors)
