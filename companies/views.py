from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, FormView
from companies.forms import CompanyForm
from django.urls import reverse_lazy, resolve
from companies.models import Company


class CompanyCreateView(CreateView):
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

    def get_queryset(self):
        return Company.objects.filter(user=self.request.user)


class CompanyDetailView(DetailView):
    template_name = 'companies/company_detail.html'
    context_object_name = 'company'
    model = Company

    def get_context_data(self, **kwargs):
        current_url = resolve(self.request.path_info).url_name
        context = super(CompanyDetailView, self).get_context_data(**kwargs)
        context['current_url'] = current_url
        return context


class CompanyUpdateView(UpdateView):
    template_name = 'companies/company_update.html'
    form_class = CompanyForm
    model = Company
    success_url = reverse_lazy('companies:list')


class CompanyDeleteView(DeleteView):
    template_name = 'companies/company_delete.html'
    success_url = reverse_lazy('accounts:profile')
    model = Company
