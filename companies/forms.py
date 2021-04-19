from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, MultiField, Div
from django import forms
from django.contrib.auth import get_user_model

from companies.models import Company

User = get_user_model()


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'description', 'address', 'email', 'phone',)

    name = forms.CharField(
        required=True,
        help_text='(Required)',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Name',
            }
        )
    )

    description = forms.CharField(
        max_length=500,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Description',
                'rows': 3
            }
        )
    )

    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Address',
            }
        )
    )

    email = forms.EmailField(
        max_length=100,
        required=True,
        help_text='(Required)',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'exapmple@domain.com'
            }
        )
    )
    phone = forms.RegexField(
        required=True,
        regex=r'^\+?1?\d{9,15}$',
        max_length=15,
        help_text='(Required)',
        widget=forms.TextInput(
            attrs={
                'placeholder': '+380999999999',
                'class': 'form-control',
            }
        )
    )

