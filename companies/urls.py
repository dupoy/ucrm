from django.urls import path

from companies.views import (CompanyCreationView,
                             CompanyDetailView,
                             CompanyUpdateView,
                             CompanyDeleteView,
                             CompanyListView,
                             )

app_name = 'companies'

urlpatterns = [
    path('add/', CompanyCreationView.as_view(), name='add'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', CompanyUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', CompanyDeleteView.as_view(), name='delete'),
    path('', CompanyListView.as_view(), name='list'),

]
