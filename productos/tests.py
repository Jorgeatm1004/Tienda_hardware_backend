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


class EditarEliminarTests(TestCase):
    def setUp(self):
        self.producto = Producto.objects.create(
            nombre='Fuente de poder EVGA 650W', descripcion='80 Plus Bronze', precio=100000, stock=8
        )

    def test_editar_get_muestra_form_con_datos(self):
        respuesta = self.client.get(reverse('producto_editar', args=[self.producto.id]))
        self.assertEqual(respuesta.status_code, 200)
        self.assertContains(respuesta, 'Fuente de poder EVGA 650W')
        self.assertContains(respuesta, 'csrfmiddlewaretoken')

    def test_editar_post_guarda_y_redirige(self):
        respuesta = self.client.post(
            reverse('producto_editar', args=[self.producto.id]),
            {'nombre': 'Fuente EVGA 750W', 'descripcion': '80 Plus Gold', 'precio': 120000, 'stock': 4},
        )
        self.assertRedirects(respuesta, reverse('catalogo'))
        self.producto.refresh_from_db()
        self.assertEqual(self.producto.nombre, 'Fuente EVGA 750W')
        self.assertEqual(self.producto.stock, 4)

    def test_editar_post_invalido_no_guarda(self):
        respuesta = self.client.post(
            reverse('producto_editar', args=[self.producto.id]),
            {'nombre': '', 'descripcion': 'x', 'precio': 1, 'stock': 1},
        )
        self.assertEqual(respuesta.status_code, 200)
        self.producto.refresh_from_db()
        self.assertEqual(self.producto.nombre, 'Fuente de poder EVGA 650W')

    def test_editar_inexistente_da_404(self):
        respuesta = self.client.get(reverse('producto_editar', args=[9999]))
        self.assertEqual(respuesta.status_code, 404)
