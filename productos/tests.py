from django.test import TestCase
from django.urls import reverse

from .forms import ProductoForm
from .models import Producto


class ProductoFormTests(TestCase):
    def test_form_valido(self):
        form = ProductoForm(data={'nombre': 'Mouse', 'descripcion': 'Mouse gamer', 'precio': 60000, 'stock': 3})
        self.assertTrue(form.is_valid())

    def test_form_sin_nombre_es_invalido(self):
        form = ProductoForm(data={'nombre': '', 'descripcion': 'x', 'precio': 1000, 'stock': 1})
        self.assertFalse(form.is_valid())
        self.assertIn('nombre', form.errors)
