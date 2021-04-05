from django.urls import path

from company.views import CompanyCreationView, CompanyDetailView

app_name = 'company'

urlpatterns = [
    path('add/', CompanyCreationView.as_view(), name='add'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='detail'),
]
