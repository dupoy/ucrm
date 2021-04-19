from django import forms

from orders.models import OrderItem, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['created_at', ]

        widgets = {
            'customer': forms.Select(
                attrs={
                    'class': 'form-control',
                }
            )
        }


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        exclude = ['order']

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
