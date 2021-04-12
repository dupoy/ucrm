from django.http import JsonResponse, HttpResponseRedirect, Http404
from django.urls import resolve, reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.views.generic.base import View

from companies.models import Company
from customers.forms import CustomerForm, ContactForm
from customers.models import Customer, Contact


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


class CustomerDetailView(DetailView, CreateView):
    template_name = 'customers/customer_detail.html'
    model = Customer
    context_object_name = 'customer'
    form_class = ContactForm

    def get_success_url(self):
        return Customer.objects.get(pk=self.kwargs.get('pk')).get_absolute_url()

    def get_context_data(self, **kwargs):
        current_url = resolve(self.request.path_info).url_name
        context = super(CustomerDetailView, self).get_context_data(**kwargs)
        context['current_url'] = current_url
        context['company'] = Company.objects.get(slug=self.kwargs.get('slug'))
        return context

    def form_valid(self, form):
        contact = form.save(commit=False)
        contact.customer = Customer.objects.get(pk=self.kwargs.get('pk'))
        contact.save()
        return super().form_valid(form)


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


class ContactDeleteView(DeleteView):
    template_name = 'customers/customer_contact_delete.html'
    model = Contact

    def get_success_url(self):
        return Customer.objects.get(pk=self.kwargs.get('customer')).get_absolute_url()
