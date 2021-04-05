from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from company.forms import CompanyCreationForm
from company.models import Company


class CompanyCreationView(CreateView):
    template_name = 'company/company_create.html'
    model = Company
    form_class = CompanyCreationForm
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
