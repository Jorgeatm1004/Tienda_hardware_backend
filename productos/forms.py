from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock']
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'precio': 'Precio (CLP)',
            'stock': 'Stock disponible',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ej: Procesador Ryzen 5 5600X'}),
            'descripcion': forms.Textarea(attrs={'rows': 4}),
            'precio': forms.NumberInput(attrs={'min': 0, 'step': 1}),
            'stock': forms.NumberInput(attrs={'min': 0}),
        }
