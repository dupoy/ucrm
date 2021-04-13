from django.urls import path

from products.views import (
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('add', ProductCreateView.as_view(), name='add'),
    path('update/<slug:slug>', ProductUpdateView.as_view(), name='update'),
    path('delete/<slug:slug>', ProductDeleteView.as_view(), name='delete'),
]
