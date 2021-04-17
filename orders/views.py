from django.shortcuts import render
from django.views.generic import ListView

from companies.models import Company
from core.mixins import LinkMixin
from orders.models import Order


class OrderListView(LinkMixin, ListView):
    template_name = 'orders/order_list.html'
    model = Order
    context_object_name = 'orders'

    def get_queryset(self):
        orders = []
        for customer in Company.objects.get(slug=self.kwargs['slug']).customers.all():
            orders.extend(customer.orders.all())
        return orders
