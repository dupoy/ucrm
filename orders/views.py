from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from companies.models import Company
from core.mixins import LinkMixin, ModelNameMixin, PreviousPageMixin
from orders.forms import OrderItemForm, OrderForm
from orders.models import Order, OrderItem
from django.db.models.functions import TruncDate


class OrderListView(LoginRequiredMixin, LinkMixin, ListView):
    template_name = 'orders/order_list.html'
    model = Order
    context_object_name = 'orders'

    def get_queryset(self):
        orders = []
        for customer in Company.objects.get(slug=self.kwargs['slug']).customers.all():
            orders.extend(customer.orders.all())
        return orders


class OrderCreateView(LoginRequiredMixin, LinkMixin, CreateView):
    template_name = 'orders/order_create.html'
    model = Order
    form_class = OrderForm

    def get_success_url(self):
        return reverse_lazy('companies:orders:add-item', kwargs={'slug': self.kwargs['slug'], 'pk': self.object.pk})


class OrderDeleteView(LoginRequiredMixin, ModelNameMixin, PreviousPageMixin, DeleteView):
    template_name = 'bases/actions/base_delete.html'
    model = Order

    def get_success_url(self):
        return reverse_lazy('companies:orders:orders', kwargs={'slug': self.kwargs['slug']})


class OrderItemCreateView(LoginRequiredMixin, LinkMixin, CreateView):
    template_name = 'orders/order_add_item.html'
    model = OrderItem
    form_class = OrderItemForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.get(pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        order = Order.objects.get(pk=self.kwargs['pk'])
        order_item = form.save(commit=False)
        if order.order_items.filter(product=order_item.product).exists():
            item = order.order_items.get(product=order_item.product)
            item.quantity += order_item.quantity
            item.save()
        else:
            order_item.order = order
            self.object = order_item.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.request.path


class OrderItemDeleteView(LoginRequiredMixin, DeleteView):
    model = OrderItem

    def get_object(self, queryset=None):
        return OrderItem.objects.get(pk=self.kwargs['item_pk'])

    def get_success_url(self):
        return reverse_lazy('companies:orders:add-item', kwargs={'slug': self.kwargs['slug'], 'pk': self.kwargs['pk']})

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


@login_required
def orders_charts(request, slug):
    labels = []
    data = []

    queryset = OrderItem.objects.filter(order__customer__company__slug=slug).annotate(
        order_date=TruncDate('order__created_at')).values('order_date').annotate(
        order_summary=Sum('total_price')
    ).order_by('-order_date')

    for entry in queryset:
        labels.append(entry['order_date'])
        data.append(entry['order_summary'])

    return JsonResponse(data={
        'labels': labels,
        'data': data
    })
