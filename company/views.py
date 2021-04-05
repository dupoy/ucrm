from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accounts.forms import UserRegistrationForm
from company.forms import CompanyForm
from company.models import Company, Manager


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
    model = Company
    success_url = reverse_lazy('accounts:profile')


class ManagerCreationView(CreateView):
    template_name = 'accounts/managers/manager_add.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('accounts:profile')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_leader = False
        user.is_manager = True
        user.save()
        Manager.objects.create(
            user=user,
            company=form['companies']
        )
        return super().form_valid(form)
