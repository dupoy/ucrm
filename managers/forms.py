from django import forms
from django.contrib.auth import get_user_model

from companies.models import Company

User = get_user_model()


class ManagerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'bio', 'avatar')

    username = forms.CharField(
        label='Enter username',
        min_length=4, max_length=50,
        help_text='(Required)',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        )
    )

    first_name = forms.CharField(
        label='Enter first name',
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
        label='Enter last name',
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

    password = forms.CharField(
        label='Enter password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        )
    )
    password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Repeat password'
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

    bio = forms.CharField(
        required=False,
        label='About you',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'About you',
                'id': 'bio'
            }
        )
    )

    companies = forms.ModelChoiceField(
        queryset=Company.objects.none(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'companies'
            }
        )
    )

    avatar = forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'id': 'avatar'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already exists.')
        return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Please use another Email, that is already taken.')
        return email


class ManagerUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'bio', 'avatar']

    username = forms.CharField(
        label='Enter username',
        min_length=4, max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Username'
            }
        )
    )

    first_name = forms.CharField(
        label='Enter first name',
        min_length=4, max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }
        )
    )

    last_name = forms.CharField(
        label='Enter last name',
        min_length=4, max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
            }
        )
    )

    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'exapmple@domain.com'
            }
        )
    )

    phone = forms.RegexField(
        label='Phone number',
        regex=r'^\+?1?\d{9,15}$',
        max_length=15,
        widget=forms.TextInput(
            attrs={
                'placeholder': '+38(099)-999-99-99',
                'class': 'form-control',
            }
        )
    )

    bio = forms.CharField(
        required=False,
        label='About you',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'About you',
                'id': 'bio'
            }
        )
    )

    avatar = forms.FileField(
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'id': 'avatar'
            }
        )
    )

    companies = forms.ModelChoiceField(
        queryset=Company.objects.none(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'companies'
            }
        )
    )