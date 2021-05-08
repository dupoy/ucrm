from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from companies.models import Company
from core.mixins import PreviousPageMixin, ModelNameMixin, LinkMixin
from customers.forms import CustomerForm
from customers.models import Customer
from products.models import Product


class CustomerListView(LoginRequiredMixin, LinkMixin, ListView):
    template_name = 'customers/customer_list.html'
    model = Customer
    context_object_name = 'customers'

    def get_queryset(self):
        return Company.objects.get(slug=self.kwargs['slug']).customers.all()


class CustomerDetailView(LoginRequiredMixin, LinkMixin, DetailView):
    template_name = 'customers/customer_detail.html'
    model = Customer
    context_object_name = 'customer'


class CustomerCreateView(LoginRequiredMixin, ModelNameMixin, PreviousPageMixin, CreateView):
    template_name = 'bases/actions/base_add.html'
    form_class = CustomerForm
    model = Customer

    def get_success_url(self):
        return reverse_lazy('companies:customers:customers', args=(self.kwargs.get('slug'),))

    def form_valid(self, form):
        customer = form.save(commit=False)
        customer.company = Company.objects.get(slug=self.kwargs.get('slug'))
        customer.save()
        return super().form_valid(form)


class CustomerUpdateView(LoginRequiredMixin, PreviousPageMixin, UpdateView):
    template_name = 'bases/actions/base_update.html'
    model = Customer
    form_class = CustomerForm

    def get_success_url(self):
        return reverse_lazy('companies:customers:customers', kwargs={'slug': self.kwargs.get('slug')})


class CustomerDeleteView(LoginRequiredMixin, PreviousPageMixin, DeleteView):
    template_name = 'bases/actions/base_delete.html'
    model = Customer

    def get_success_url(self):
        return reverse_lazy('companies:customers:customers', kwargs={'slug': self.kwargs.get('slug')})


@login_required
def remove_preferred_product(request, slug, pk, pk_product):
    customer = get_object_or_404(Customer, pk=pk)
    product = get_object_or_404(Product, pk=pk_product)
    customer.preferred_products.remove(product)
    customer.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
