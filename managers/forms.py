from django import forms
from django.contrib.auth import get_user_model

from companies.models import Company

User = get_user_model()


class ManagerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'about', 'avatar')

    first_name = forms.CharField(
        min_length=4, max_length=50,
        help_text='(Required)',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }
        )
    )

    last_name = forms.CharField(
        min_length=4, max_length=50,
        help_text='(Required)',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }
        )
    )

    email = forms.EmailField(
        max_length=100,
        help_text='(Required)',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        )
    )

    phone = forms.RegexField(
        label='Phone number',
        regex=r'^\+?1?\d{9,15}$',
        max_length=15,
        help_text='(Required)',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    about = forms.CharField(
        required=False,
        label='About you',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'About you',
            }
        )
    )

    avatar = forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Please use another Email, that is already taken.')
        return email


