from django.urls import path

from company.views import (CompanyCreationView, CompanyDetailView, ManagerCreateView, CompanyUpdateView,
                           CompanyDeleteView, ManagerDeleteView, ManagerUpdateView)

app_name = 'company'

urlpatterns = [
    path('add/', CompanyCreationView.as_view(), name='add'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', CompanyUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CompanyDeleteView.as_view(), name='delete'),
    path('add-manager/', ManagerCreateView.as_view(), name='add-manager'),
    path('<int:pk>/update-manager/', ManagerUpdateView.as_view(), name='update-manager'),
    path('<int:pk>/delete-manager/', ManagerDeleteView.as_view(), name='delete-manager'),

]
