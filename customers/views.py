from django.http import JsonResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404
from django.urls import resolve, reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.views.generic.base import View

from companies.models import Company
from customers.forms import CustomerForm
from customers.models import Customer
from products.models import Product


class CustomerListView(ListView):
    template_name = 'customers/customer_list.html'
    model = Customer
    context_object_name = 'customers'

    def get_queryset(self):
        return Company.objects.get(slug=self.kwargs['slug']).customers.all()

    def get_context_data(self, **kwargs):
        current_url = resolve(self.request.path_info).url_name
        context = super(CustomerListView, self).get_context_data(**kwargs)
        context['current_url'] = current_url
        context['company'] = Company.objects.get(slug=self.kwargs.get('slug'))
        return context


class CustomerDetailView(DetailView):
    template_name = 'customers/customer_detail.html'
    model = Customer
    context_object_name = 'customer'

    def get_context_data(self, **kwargs):
        current_url = resolve(self.request.path_info).url_name
        context = super(CustomerDetailView, self).get_context_data(**kwargs)
        context['current_url'] = current_url
        context['company'] = Company.objects.get(slug=self.kwargs.get('slug'))
        return context


class CustomerCreateView(CreateView):
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

    def get_context_data(self, **kwargs):
        context = super(CustomerCreateView, self).get_context_data(**kwargs)
        context['previous'] = self.request.META.get('HTTP_REFERER')
        context['model_name'] = self.model.__name__
        return context


class CustomerUpdateView(UpdateView):
    template_name = 'bases/actions/base_update.html'
    model = Customer
    form_class = CustomerForm

    def get_success_url(self):
        return reverse_lazy('companies:customers:customers', kwargs={'slug': self.kwargs.get('slug')})

    def get_context_data(self, **kwargs):
        context = super(CustomerUpdateView, self).get_context_data(**kwargs)
        context['previous'] = self.request.META.get('HTTP_REFERER')
        return context


class CustomerDeleteView(DeleteView):
    template_name = 'bases/actions/base_delete.html'
    model = Customer

    def get_success_url(self):
        return reverse_lazy('companies:customers:customers', kwargs={'slug': self.kwargs.get('slug')})

    def get_context_data(self, **kwargs):
        context = super(CustomerDeleteView, self).get_context_data(**kwargs)
        context['previous'] = self.request.META.get('HTTP_REFERER')
        return context


def remove_preferred_product(request, slug, pk, pk_product):
    customer = get_object_or_404(Customer, pk=pk)
    product = get_object_or_404(Product, pk=pk_product)
    customer.preferred_products.remove(product)
    customer.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
