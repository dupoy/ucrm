from django.urls import path

from company.views import CompanyCreationView, CompanyDetailView, ManagerCreationView

app_name = 'company'

urlpatterns = [
    path('add/', CompanyCreationView.as_view(), name='add'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='detail'),
    path('add-manager/', ManagerCreationView.as_view(), name='add-manager'),

]
