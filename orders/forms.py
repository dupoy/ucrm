from django import forms

from core.forms import DateTimePicker
from orders.models import OrderItem, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'customer': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'created_at': DateTimePicker(
                attrs={
                    'id': 'datetime-id',
                    'class': 'form-control',
                }
            ),
        }


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        exclude = ['order', 'total_price']

        widgets = {
            'product': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            ),
            'quantity': forms.Select(
                choices=[(i, i) for i in range(1, 10)],
                attrs={
                    'class': 'form-control'
                }
            )

        }
