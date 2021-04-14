from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, FormView
from companies.forms import CompanyForm
from django.urls import reverse_lazy, resolve
from companies.models import Company
from core.mixins import PreviousPageMixin, ModelNameMixin, LinkMixin


class CompanyCreateView(ModelNameMixin, PreviousPageMixin, CreateView):
    template_name = 'bases/actions/base_add.html'
    form_class = CompanyForm
    model = Company
    success_url = reverse_lazy('companies:list')

    def form_valid(self, form):
        company = form.save(commit=False)
        company.user = self.request.user
        company.save()
        return super().form_valid(form)


class CompanyListView(ListView):
    template_name = 'companies/company_list.html'
    model = Company
    context_object_name = 'companies'

    def get_queryset(self):
        return Company.objects.filter(user=self.request.user)


class CompanyDetailView(LinkMixin, DetailView):
    template_name = 'companies/company_detail.html'
    context_object_name = 'company'
    model = Company


class CompanyUpdateView(PreviousPageMixin, UpdateView):
    template_name = 'bases/actions/base_update.html'
    form_class = CompanyForm
    model = Company
    success_url = reverse_lazy('accounts:companies')


class CompanyDeleteView(PreviousPageMixin, DeleteView):
    template_name = 'bases/actions/base_delete.html'
    success_url = reverse_lazy('accounts:profile')
    model = Company
