from django.views.generic import DeleteView, CreateView, UpdateView

from contacts.forms import ContactForm, ContactHistoryForm
from contacts.models import Contact, ContactHistory
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
    template_name = 'contacts/contact_delete.html'
    model = Contact

    def get_success_url(self):
        return Customer.objects.get(pk=self.kwargs.get('id')).get_absolute_url()


class ContactUpdateView(UpdateView):
    template_name = 'contacts/contact_update.html'
    form_class = ContactForm
    model = Contact

    def get_success_url(self):
        return Customer.objects.get(pk=self.kwargs.get('id')).get_absolute_url()


class ContactHistoryCreate(CreateView):
    template_name = 'contacts/contact_add.html'
    model = ContactHistory

    def get_success_url(self):
        return Customer.objects.get(pk=self.kwargs.get('pk')).get_absolute_url()

    def get_form(self, form_class=ContactHistoryForm):
        form = super(ContactHistoryCreate, self).get_form(form_class)
        form.fields['contact'].queryset = Customer.objects.get(pk=self.kwargs.get('pk')).contacts
        return form

    def form_valid(self, form):
        contact_history = form.save(commit=False)
        contact_history.manager = self.request.user
        contact_history.save()
        return super().form_valid(form)


class ContactHistoryUpdate(UpdateView):
    template_name = 'contacts/contact_update.html'
    model = ContactHistory

    def get_success_url(self):
        return Customer.objects.get(pk=self.kwargs.get('id')).get_absolute_url()

    def get_form(self, form_class=ContactHistoryForm):
        form = super(ContactHistoryUpdate, self).get_form(form_class)
        form.fields['contact'].queryset = Customer.objects.get(pk=self.kwargs.get('id')).contacts
        return form

    def form_valid(self, form):
        contact_history = form.save(commit=False)
        contact_history.manager = self.request.user
        contact_history.save()
        return super().form_valid(form)


class ContactHistoryDelete(DeleteView):
    template_name = 'contacts/contact_delete.html'
    model = ContactHistory

    def get_success_url(self):
        return Customer.objects.get(pk=self.kwargs.get('id')).get_absolute_url()
