from django.urls import path, include

from companies.views import CompanyDetailView

app_name = 'companies'

urlpatterns = [
    path('', CompanyDetailView.as_view(), name='detail'),
    path('managers/', include('managers.urls', namespace='managers')),
    path('products/', include('products.urls', namespace='products')),
    path('customers/', include('customers.urls', namespace='customers')),
]
