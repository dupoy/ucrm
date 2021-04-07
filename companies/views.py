from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, FormView
from companies.forms import CompanyForm
from django.urls import reverse_lazy
from companies.models import Company


class CompanyCreationView(CreateView):
    template_name = 'companies/company_create.html'
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

    def queryset(self):
        return Company.objects.filter(user=self.request.user)


class CompanyDetailView(DetailView):
    template_name = 'companies/company_detail.html'
    context_object_name = 'companies'
    model = Company


class CompanyUpdateView(UpdateView):
    template_name = 'companies/company_update.html'
    form_class = CompanyForm
    model = Company
    success_url = reverse_lazy('accounts:profile')


class CompanyDeleteView(DeleteView):
    template_name = 'companies/company_delete.html'
    success_url = reverse_lazy('accounts:profile')
    model = Company
