from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm

User = get_user_model()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'id': 'login-username'
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-password'
        }
    ))


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'bio', 'avatar')

    username = forms.CharField(
        label='Enter username',
        min_length=4, max_length=50,
        help_text='Required',
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
        help_text='Required',
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
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
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
        error_messages={
            'required': "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        },
        max_length=15,
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    bio = forms.CharField(
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
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'id': 'avatar'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username is already .exists.')
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


class UserPasswordResetForm(PasswordResetForm):
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

    def clean_email(self):
        email = self.cleaned_data['email']
        test = User.objects.filter(email=email)
        if not test:
            raise forms.ValidationError('Unfortunately we can not find that email address')
        return email


class UserPasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'New password',
                'id': 'form-new-pass'
            }
        )
    )
    new_password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Repeat password',
                'id': 'form-new-pass2'
            }
        )
    )


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Old Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Old password',
                'id': 'form-old-pass'
            }
        )
    )
    new_password1 = forms.CharField(
        label='New password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'New password',
                'id': 'form-new-pass'
            }
        )
    )
    new_password2 = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'New password',
                'id': 'form-new-pass2'
            }
        )
    )


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'phone', 'bio', 'avatar']

    username = forms.CharField(
        label='Enter username',
        min_length=4, max_length=50,
        help_text='Required',
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
        help_text='Required',
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
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last name'
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
        label='Phone number',
        regex=r'^\+?1?\d{9,15}$',
        error_messages={
            'required': "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
        },
        max_length=15,
        help_text='Required',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    bio = forms.CharField(
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
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'id': 'avatar'
            }
        )
    )
