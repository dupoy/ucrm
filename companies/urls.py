from django.urls import path

from companies.views import CompanyDetailView


app_name = 'companies'

urlpatterns = [
    path('', CompanyDetailView.as_view(), name='detail'),
]
