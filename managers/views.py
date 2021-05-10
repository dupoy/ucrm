from django.contrib.auth.base_user import BaseUserManager
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from companies.models import Company
from core.mixins import PreviousPageMixin, ModelNameMixin, LinkMixin, PermissionMixin
from managers.forms import ManagerForm
from django.contrib.auth import get_user_model
from companies.mixins import AtomicMixin
from django.urls import reverse_lazy
from managers.models import Manager

User = get_user_model()


class ManagerListView(PermissionMixin, LinkMixin, ListView):
    template_name = 'managers/manager_company_list.html'
    model = Manager
    context_object_name = 'managers'

    def get_queryset(self):
        if 'slug' not in self.kwargs:
            managers = []
            for company in self.request.user.companies.all():
                managers.extend(company.managers.all())
            return managers
        else:
            return Company.objects.get(slug=self.kwargs.get('slug')).managers.all()


class ManagerCreateView(PermissionMixin, AtomicMixin, ModelNameMixin, PreviousPageMixin, CreateView):
    model = Manager
    template_name = 'bases/actions/base_add.html'
    form_class = ManagerForm

    def get_success_url(self):
        return reverse_lazy('companies:managers:managers', kwargs={'slug': self.kwargs.get('slug')})

    def form_valid(self, form):
        password = BaseUserManager().make_random_password()
        user = form.save(commit=False)
        user.set_password(password)
        user.is_manager = True
        user.save()
        Manager.objects.create(
            user=user,
            company=Company.objects.get(slug=self.kwargs.get('slug'))
        )

        current_site = get_current_site(self.request)
        subject = 'Your are invited to be an manager'
        message = render_to_string('managers/mail.html', {
            'message': 'You were added as an agent do UCRM. Please come login to start working.',
            'name': user.get_name(),
            'email': user.email,
            'password': password,
            'domain': current_site.domain,
        })
        user.email_user(subject=subject, message=message)

        return super().form_valid(form)


class ManagerDeleteView(PermissionMixin, PreviousPageMixin, DeleteView):
    template_name = 'bases/actions/base_delete.html'
    model = User

    def get_success_url(self):
        return reverse_lazy('companies:managers:managers', kwargs={'slug': self.kwargs.get('slug')})


class ManagerUpdateView(PermissionMixin, PreviousPageMixin, UpdateView):
    template_name = 'bases/actions/base_update.html'
    form_class = ManagerForm
    model = User

    def get_success_url(self):
        return reverse_lazy('companies:managers:managers', kwargs={'slug': self.kwargs.get('slug')})
