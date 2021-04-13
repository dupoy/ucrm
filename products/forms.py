from django import forms

from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['company', 'slug']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3,
                }
            ),
            'price': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                }
            )
        }
