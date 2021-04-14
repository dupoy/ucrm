from django.urls import path, include

from customers.views import (
    CustomerListView,
    CustomerCreateView,
    CustomerDeleteView,
    CustomerUpdateView,
    CustomerDetailView,
)

app_name = 'customers'

urlpatterns = [
    path('', CustomerListView.as_view(), name='customers'),
    path('add/', CustomerCreateView.as_view(), name='add'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', CustomerUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CustomerDeleteView.as_view(), name='delete'),

    path('<int:pk>/contacts/', include('contacts.urls', namespace='contacts')),
]
