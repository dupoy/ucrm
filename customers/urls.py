from django.urls import path

from customers.views import (
    CustomerListView,
    CustomerCreateView,
    CustomerDeleteView,
    CustomerUpdateView,
    CustomerDetailView,
)

app_name = 'customers'

urlpatterns = [
    path('<slug:slug>/', CustomerListView.as_view(), name='customers'),
    path('<slug:slug>/add', CustomerCreateView.as_view(), name='add'),
    path('<slug:slug>/<int:pk>', CustomerDetailView.as_view(), name='detail'),
    path('<slug:slug>/<int:pk>/update', CustomerUpdateView.as_view(), name='update'),
    path('<slug:slug>/<int:pk>/delete', CustomerDeleteView.as_view(), name='delete'),
]
