from django.views.generic import DeleteView, CreateView, UpdateView

from contacts.forms import ContactForm, ContactHistoryForm
from contacts.models import Contact, ContactHistory
from core.mixins import PreviousPageMixin, ModelNameMixin
from customers.models import Customer


class ContactCreateView(ModelNameMixin, PreviousPageMixin, CreateView):
    template_name = 'bases/actions/base_add.html'
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


class ContactUpdateView(PreviousPageMixin, UpdateView):
    template_name = 'bases/actions/base_update.html'
    form_class = ContactForm
    model = Contact

    def get_object(self, queryset=None):
        return Contact.objects.get(pk=self.kwargs.get('pk_contact'))

    def get_success_url(self):
        return Customer.objects.get(pk=self.kwargs.get('pk')).get_absolute_url()


class ContactDeleteView(PreviousPageMixin, DeleteView):
    template_name = 'bases/actions/base_delete.html'
    model = Contact

    def get_object(self, queryset=None):
        return Contact.objects.get(pk=self.kwargs.get('pk_contact'))

    def get_success_url(self):
        return Customer.objects.get(pk=self.kwargs.get('pk')).get_absolute_url()


class ContactHistoryCreate(ModelNameMixin, PreviousPageMixin, CreateView):
    template_name = 'bases/actions/base_add.html'
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


class ContactHistoryUpdate(PreviousPageMixin, UpdateView):
    template_name = 'bases/actions/base_update.html'
    model = ContactHistory

    def get_object(self, queryset=None):
        return ContactHistory.objects.get(pk=self.kwargs.get('pk_contact_history'))

    def get_success_url(self):
        return Customer.objects.get(pk=self.kwargs.get('pk')).get_absolute_url()

    def get_form(self, form_class=ContactHistoryForm):
        form = super(ContactHistoryUpdate, self).get_form(form_class)
        form.fields['contact'].queryset = Customer.objects.get(pk=self.kwargs.get('pk')).contacts
        return form

    def form_valid(self, form):
        contact_history = form.save(commit=False)
        contact_history.manager = self.request.user
        contact_history.save()
        return super().form_valid(form)


class ContactHistoryDelete(PreviousPageMixin, DeleteView):
    template_name = 'bases/actions/base_delete.html'
    model = ContactHistory

    def get_object(self, queryset=None):
        return ContactHistory.objects.get(pk=self.kwargs.get('pk_contact_history'))

    def get_success_url(self):
        return Customer.objects.get(pk=self.kwargs.get('pk')).get_absolute_url()
