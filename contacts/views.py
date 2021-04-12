from django.views.generic import DeleteView, CreateView

from contacts.forms import ContactForm
from contacts.models import Contact
from customers.models import Customer


class ContactCreateView(CreateView):
    template_name = 'contacts/contact_add.html'
    model = Contact
    form_class = ContactForm

    def get_success_url(self):
        customer = self.object.customer
        return customer.get_absolute_url()

    def form_valid(self, form):
        contact = form.save(commit=False)
        contact.customer = Customer.objects.get(pk=self.kwargs.get('pk'))
        contact.save()
        return super().form_valid(form)


class ContactDeleteView(DeleteView):
    template_name = 'customers/customer_contact_delete.html'
    model = Contact

    def get_success_url(self):
        return Customer.objects.get(pk=self.kwargs.get('id')).get_absolute_url()
