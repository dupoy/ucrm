from django.views.generic import CreateView, DeleteView, UpdateView
from managers.forms import ManagerForm, ManagerUpdateForm
from django.contrib.auth import get_user_model
from companies.mixins import AtomicMixin
from django.urls import reverse_lazy
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
    success_url = reverse_lazy('accounts:profile')
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
