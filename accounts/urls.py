from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView,
    PasswordResetConfirmView, PasswordChangeView,
)
from accounts.forms import UserPasswordResetForm, UserPasswordResetConfirmForm, UserPasswordChangeForm, UserLoginForm
from accounts.views import ProfileView, activate, UserRegistrationView
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    path('sign-in/',
         LoginView.as_view(
             template_name='registration/login.html',
             authentication_form=UserLoginForm),
         name='login'),

    path('sign-off/',
         LogoutView.as_view(
             template_name='registration/logout.html'),
         name='logout'),

    path('password-reset/',
         PasswordResetView.as_view(
             template_name='registration/password_reset_form.html',
             form_class=UserPasswordResetForm),
         name='password-reset'),

    path('password-reset-confirm/<uidb64>/<token>',
         PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html',
             form_class=UserPasswordResetConfirmForm),
         name="password-reset-confirm"),

    path('password_change/',
         PasswordChangeView.as_view(
             template_name="registration/password_change_form.html",
             form_class=UserPasswordChangeForm),
         name='password-change'),

    path('profile/', ProfileView.as_view(), name='profile'),
    path('sign-up/', UserRegistrationView.as_view(), name='registration'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]
