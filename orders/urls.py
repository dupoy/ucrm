from django.urls import path

from orders.views import (
    OrderListView,
    OrderCreateView,
    OrderDeleteView,
    OrderItemCreateView,
    OrderItemDeleteView,
)

app_name = 'orders'

urlpatterns = [
    path('', OrderListView.as_view(), name='orders'),
    path('add/', OrderCreateView.as_view(), name='add'),
    path('delete/<int:pk>', OrderDeleteView.as_view(), name='delete'),
    path('<int:pk>/add-item', OrderItemCreateView.as_view(), name='add-item'),
    path('<int:pk>/<int:item_pk>/remove-item', OrderItemDeleteView.as_view(), name='remove-item'),
]
