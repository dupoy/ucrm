from django.urls import path

from company.views import CompanyCreationView, CompanyDetailView, ManagerCreationView, CompanyUpdateView, CompanyDeleteView

app_name = 'company'

urlpatterns = [
    path('add/', CompanyCreationView.as_view(), name='add'),
    path('<int:pk>/', CompanyDetailView.as_view(), name='detail'),
    path('<int:pk>/update/', CompanyUpdateView.as_view(), name='update'),
    path('<int:pk>/deelte/', CompanyDeleteView.as_view(), name='delete'),
    path('add-manager/', ManagerCreationView.as_view(), name='add-manager'),

]
