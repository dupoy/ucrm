from django.contrib.auth.base_user import BaseUserManager
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView

from companies.models import Company
from customers.models import Customer
from managers.forms import ManagerForm, ManagerUpdateForm
from django.contrib.auth import get_user_model
from companies.mixins import AtomicMixin
from django.urls import reverse_lazy, resolve
from managers.models import Manager

User = get_user_model()


class ManagerCreateView(AtomicMixin, CreateView):
    model = User
    template_name = 'managers/manager_add.html'
    form_class = ManagerForm

    def get_success_url(self):
        return reverse_lazy('managers:managers', kwargs={'slug': self.kwargs.get('company_slug')})

    def form_valid(self, form):
        password = BaseUserManager().make_random_password()
        user = form.save(commit=False)
        user.set_password(password)
        user.is_leader = False
        user.is_manager = True
        user.save()
        Manager.objects.create(
            user=user,
            company=Company.objects.get(slug=self.kwargs.get('company_slug'))
        )
        send_mail(
            subject='Your are invited to be an manager',
            message='You were added as an agent do UCRM. Please come login to start working.',
            from_email='admin@test.com',
            recipient_list=[user.email]
        )
        current_site = get_current_site(self.request)
        subject = 'You are invited to be an manager'
        message = render_to_string('managers/mail.html', {
            'user': user,
            'domain': current_site.domain,
            'password': password
        })
        user.email_user(subject=subject, message=message)

        return super().form_valid(form)


class ManagerDeleteView(DeleteView):
    template_name = 'managers/manager_delete.html'
    model = User

    def get_success_url(self):
        return reverse_lazy('managers:managers', kwargs={'slug': self.kwargs.get('company_slug')})


class ManagerUpdateView(UpdateView):
    template_name = 'managers/manager_update.html'
    model = User

    def get_success_url(self):
        return reverse_lazy('managers:managers', kwargs={'slug': self.kwargs.get('company_slug')})

    def get_form(self, form_class=ManagerUpdateForm):
        form = super(ManagerUpdateView, self).get_form(form_class)
        form.fields['companies'].queryset = self.request.user.companies
        return form

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_leader = False
        user.is_manager = True
        user.save()

        manager = Manager.objects.get(user=user)
        manager.company = form.cleaned_data['companies']
        manager.save()

        return super().form_valid(form)


class ManagerListView(ListView):
    template_name = 'companies/company_managers.html'
    model = Manager
    context_object_name = 'managers'

    def get_queryset(self):
        return Company.objects.get(slug=self.kwargs.get('company_slug')).managers.all()

    def get_context_data(self, **kwargs):
        current_url = resolve(self.request.path_info).url_name
        context = super(ManagerListView, self).get_context_data(**kwargs)
        context['current_url'] = current_url
        context['company'] = Company.objects.get(slug=self.kwargs.get('company_slug'))
        return context

