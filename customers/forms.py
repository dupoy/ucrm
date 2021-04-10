from django import forms
from django.forms.widgets import Input

from customers.models import Customer


class DatePicker(Input):
    input_type = 'date'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ['company']
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'date_of_birth': 'Date of birth',
            'email': 'Email address',
            'phone': 'Phone number',
            'note': 'Note',
        }
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'First name',
                    'class': 'form-control',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Last name',
                    'class': 'form-control',
                }
            ),
            'date_of_birth': DatePicker(
                attrs={
                    'class': 'form-control datepicker',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'exapmple@domain.com'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '+38(099)9999999',
                }
            ),
            'note': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Some notes..',
                    'rows': '3',
                }
            ),
        }

