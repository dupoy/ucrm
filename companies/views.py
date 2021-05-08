from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from companies.forms import CompanyForm
from django.urls import reverse_lazy
from companies.models import Company
from core.mixins import PreviousPageMixin, ModelNameMixin, LinkMixin, PermissionMixin


class CompanyCreateView(PermissionMixin, ModelNameMixin, PreviousPageMixin, CreateView):
    template_name = 'bases/actions/base_add.html'
    form_class = CompanyForm
    model = Company
    success_url = reverse_lazy('accounts:companies')

    def form_valid(self, form):
        company = form.save(commit=False)
        company.user = self.request.user
        company.save()
        return super().form_valid(form)


class CompanyListView(PermissionMixin, ListView):
    template_name = 'companies/company_list.html'
    model = Company
    context_object_name = 'companies'

    def get_queryset(self):
        return Company.objects.filter(user=self.request.user)


class CompanyDetailView(LoginRequiredMixin, LinkMixin, DetailView):
    template_name = 'companies/company_detail.html'
    context_object_name = 'company'
    model = Company


class CompanyUpdateView(PermissionMixin, PreviousPageMixin, UpdateView):
    template_name = 'bases/actions/base_update.html'
    form_class = CompanyForm
    model = Company
    success_url = reverse_lazy('accounts:companies')


class CompanyDeleteView(PermissionMixin, PreviousPageMixin, DeleteView):
    template_name = 'bases/actions/base_delete.html'
    success_url = reverse_lazy('accounts:profile')
    model = Company
