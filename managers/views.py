from django.views.generic import CreateView, DeleteView, UpdateView, ListView

from companies.models import Company
from managers.forms import ManagerForm, ManagerUpdateForm
from django.contrib.auth import get_user_model
from companies.mixins import AtomicMixin
from django.urls import reverse_lazy, resolve
from managers.models import Manager

User = get_user_model()


class ManagerCreateView(AtomicMixin, CreateView):
    model = User
    template_name = 'managers/manager_add.html'

    def get_success_url(self):
        return self.object.manager.company.get_absolute_url()

    def get_form(self, form_class=ManagerForm):
        form = super(ManagerCreateView, self).get_form(form_class)
        form.fields['companies'].queryset = self.request.user.companies
        return form

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.is_leader = False
        user.is_manager = True
        user.save()
        Manager.objects.create(
            user=user,
            company=form.cleaned_data['companies']
        )

        return super().form_valid(form)


class ManagerDeleteView(DeleteView):
    template_name = 'managers/manager_delete.html'
    model = User

    def get_success_url(self):
        return self.object.manager.company.get_absolute_url()


class ManagerUpdateView(UpdateView):
    template_name = 'managers/manager_update.html'
    model = User

    def get_success_url(self):
        return self.object.manager.company.get_absolute_url()

    def get_form(self, form_class=ManagerUpdateForm):
        form = super(ManagerUpdateView, self).get_form(form_class)
        form.fields['companies'].queryset = self.request.user.get_company_list
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
        return Manager.objects.filter(company__slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        current_url = resolve(self.request.path_info).url_name
        context = super(ManagerListView, self).get_context_data(**kwargs)
        context['current_url'] = current_url
        context['company'] = Company.objects.get(slug=self.kwargs.get('slug'))
        return context
