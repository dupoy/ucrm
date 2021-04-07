from django import forms
from django.contrib.auth import get_user_model

from companies.models import Company

User = get_user_model()


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ('name', 'description', 'address', 'email', 'phone',)

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Company name',
                'id': 'name'
            }
        )
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Company description',
                'id': 'description'
            }
        )
    )

    address = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Company address',
                'id': 'description'
            }
        )
    )

    email = forms.EmailField(
        max_length=100,
        help_text='Required',
        error_messages={
            'required': 'Sorry, you will need an email'
        },
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )
    phone = forms.RegexField(
        regex=r'^\+?1?\d{9,15}$',
        error_messages={
            'required': "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        },
        max_length=15,
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Company phone number',
                'class': 'form-control',
            }
        )
    )


