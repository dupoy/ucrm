from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm

from companies.models import Company

User = get_user_model()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'id': 'login-username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'id': 'login-password'
        }
    ))


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone', 'about', 'avatar')

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

    about = forms.CharField(
        required=False,
        label='About you',
        max_length=500,
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


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        max_length=100,
        help_text='(Required)',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'exapmple@domain.com'
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        test = User.objects.filter(email=email)
        if not test:
            raise forms.ValidationError('Unfortunately we can not find that email address')
        return email


class UserPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }
        )
    )
    new_password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Repeat password',
            }
        )
    )


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }
        )
    )
    new_password1 = forms.CharField(
        label='New password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }
        )
    )
    new_password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Repeat password',
            }
        )
    )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'about', 'avatar']

    first_name = forms.CharField(
        min_length=4, max_length=50,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'First name'
            }
        )
    )

    last_name = forms.CharField(
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

    about = forms.CharField(
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
