from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordResetView,
    PasswordResetConfirmView, PasswordChangeView,
)
from accounts.forms import UserPasswordResetForm, UserPasswordResetConfirmForm, UserPasswordChangeForm, UserLoginForm
from accounts.views import UserProfileView, activate, UserRegistrationView, UserUpdateView, UserDeleteView
from django.urls import path
from companies.views import CompanyListView, CompanyCreateView, CompanyUpdateView, CompanyDeleteView
from managers.views import ManagerListView

app_name = 'accounts'

urlpatterns = [
    path('login/',
         LoginView.as_view(
             template_name='registration/login.html',
             authentication_form=UserLoginForm),
         name='login'),

    path('logout/',
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

    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),

    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/update/<int:pk>/', UserUpdateView.as_view(), name='profile-update'),
    path('profile/delete/<int:pk>/', UserDeleteView.as_view(), name='profile-delete'),

    path('profile/companies/', CompanyListView.as_view(), name='companies'),
    path('profile/managers/', ManagerListView.as_view(template_name='managers/manager_list.html'), name='managers'),
    path('profile/companies/add/', CompanyCreateView.as_view(), name='companies-add'),
    path('profile/companies/update/<slug:slug>/', CompanyUpdateView.as_view(), name='companies-update'),
    path('profile/companies/delete/<slug:slug>/', CompanyDeleteView.as_view(), name='companies-delete'),
]
