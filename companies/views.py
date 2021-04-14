from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, FormView
from companies.forms import CompanyForm
from django.urls import reverse_lazy, resolve
from companies.models import Company


class CompanyCreateView(CreateView):
    template_name = 'bases/actions/base_add.html'
    form_class = CompanyForm
    model = Company
    success_url = reverse_lazy('companies:list')

    def form_valid(self, form):
        company = form.save(commit=False)
        company.user = self.request.user
        company.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CompanyCreateView, self).get_context_data(**kwargs)
        context['previous'] = self.request.META.get('HTTP_REFERER')
        context['model_name'] = self.model.__name__
        return context


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
    template_name = 'bases/actions/base_update.html'
    form_class = CompanyForm
    model = Company
    success_url = reverse_lazy('accounts:companies')

    def get_context_data(self, **kwargs):
        context = super(CompanyUpdateView, self).get_context_data(**kwargs)
        context['previous'] = self.request.META.get('HTTP_REFERER')
        context['model_name'] = self.model.__name__
        return context


class CompanyDeleteView(DeleteView):
    template_name = 'bases/actions/base_delete.html'
    success_url = reverse_lazy('accounts:profile')
    model = Company

    def get_context_data(self, **kwargs):
        context = super(CompanyDeleteView, self).get_context_data(**kwargs)
        context['previous'] = self.request.META.get('HTTP_REFERER')
        context['model_name'] = self.model.__name__
        return context
