from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accounts.forms import UserRegistrationForm, UserUpdateForm
from company.forms import CompanyForm
from company.mixins import AtomicMixin
from company.models import Company, Manager, User

HTTP_REFERER = None


class CompanyCreationView(CreateView):
    template_name = 'company/company_create.html'
    form_class = CompanyForm
    model = Company
    success_url = reverse_lazy('accounts:profile')

    def form_valid(self, form):
        company = form.save(commit=False)
        company.user = self.request.user
        company.save()
        return super().form_valid(form)


class CompanyDetailView(DetailView):
    template_name = 'company/company_detail.html'
    context_object_name = 'company'
    model = Company


class CompanyUpdateView(UpdateView):
    template_name = 'company/company_update.html'
    form_class = CompanyForm
    model = Company
    success_url = reverse_lazy('accounts:profile')


class CompanyDeleteView(DeleteView):
    template_name = 'company/company_delete.html'
    success_url = reverse_lazy('accounts:profile')
    model = Company


class ManagerCreateView(AtomicMixin, CreateView):
    model = User
    template_name = 'managers/manager_add.html'

    def get_form(self, form_class=UserRegistrationForm):
        form = super(ManagerCreateView, self).get_form(form_class)
        form.fields['companies'].queryset = self.request.user.companies
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

        self.success_url = manager.company.get_absolute_url()

        return super().form_valid(form)
