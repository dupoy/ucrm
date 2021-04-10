from django.shortcuts import render
from django.urls import resolve, reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from companies.models import Company
from customers.forms import CustomerForm
from customers.models import Customer


class CustomerListView(ListView):
    template_name = 'companies/company_customers.html'
    model = Customer
    context_object_name = 'customers'

    def get_queryset(self):
        return Customer.objects.filter(company__slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        current_url = resolve(self.request.path_info).url_name
        context = super(CustomerListView, self).get_context_data(**kwargs)
        context['current_url'] = current_url
        context['company'] = Company.objects.get(slug=self.kwargs.get('slug'))
        return context


class CustomerCreateView(CreateView):
    template_name = 'customers/customer_add.html'
    form_class = CustomerForm
    model = Customer

    def get_success_url(self):
        return reverse_lazy('customers:customers', args=(self.kwargs.get('slug'),))

    def form_valid(self, form):
        customer = form.save(commit=False)
        customer.company = Company.objects.get(slug=self.kwargs.get('slug'))
        customer.save()
        return super().form_valid(form)


class CustomerUpdateView(UpdateView):
    template_name = 'customers/customer_update.html'
    model = Customer
    form_class = CustomerForm

    def get_success_url(self):
        return reverse_lazy('customers:customers', kwargs={'slug': self.kwargs.get('slug')})


class CustomerDeleteView(DeleteView):
    template_name = 'customers/customer_delete.html'
    model = Customer

    def get_success_url(self):
        return reverse_lazy('customers:customers', kwargs={'slug': self.kwargs.get('slug')})
