from django.views.generic import CreateView, DeleteView, UpdateView
from accounts.forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import get_user_model
from companies.mixins import AtomicMixin
from django.urls import reverse_lazy
from managers.models import Manager

User = get_user_model()


class ManagerCreateView(AtomicMixin, CreateView):
    model = User
    template_name = 'managers/manager_add.html'

    def get_form(self, form_class=UserRegistrationForm):
        form = super(ManagerCreateView, self).get_form(form_class)
        form.fields['companies'].queryset = self.request.user.get_company_list
        return form

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_leader = False
        user.is_manager = True
        user.save()
        manager = Manager.objects.create(
            user=user,
            company=form.cleaned_data['companies']
        )

        self.success_url = manager.company.get_absolute_url()

        return super().form_valid(form)


class ManagerDeleteView(DeleteView):
    template_name = 'managers/manager_delete.html'
    success_url = reverse_lazy('accounts:profile')
    model = User


class ManagerUpdateView(UpdateView):
    template_name = 'managers/manager_update.html'
    model = User

    def get_form(self, form_class=UserUpdateForm):
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

        self.success_url = manager.company.get_absolute_url()

        return super().form_valid(form)
