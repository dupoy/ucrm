from django.urls import path

from companies.views import (CompanyCreateView,
                             CompanyDetailView,
                             CompanyUpdateView,
                             CompanyDeleteView,
                             CompanyListView,
                             )

app_name = 'companies'

urlpatterns = [
    path('add/', CompanyCreateView.as_view(), name='add'),
    path('<slug:slug>/', CompanyDetailView.as_view(), name='detail'),
    path('<slug:slug>/update/', CompanyUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', CompanyDeleteView.as_view(), name='delete'),
    path('', CompanyListView.as_view(), name='list'),

]
