from django.shortcuts import render
from django.urls import reverse_lazy, resolve
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from companies.models import Company
from products.forms import ProductForm
from products.models import Product


class ProductCreateView(CreateView):
    template_name = 'bases/actions/base_add.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy('companies:products:products', kwargs={'slug': self.kwargs.get('slug')})

    def form_valid(self, form):
        product = form.save(commit=False)
        product.company = Company.objects.get(slug=self.kwargs['slug'])
        product.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['previous'] = self.request.META.get('HTTP_REFERER')
        context['model_name'] = self.model.__name__
        return context


class ProductListView(ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    model = Product

    def get_context_data(self, **kwargs):
        current_url = resolve(self.request.path_info).url_name
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['company'] = Company.objects.get(slug=self.kwargs['slug'])
        context['current_url'] = current_url
        return context

    def get_queryset(self):
        return Company.objects.get(slug=self.kwargs['slug']).products.all()


class ProductUpdateView(UpdateView):
    template_name = 'bases/actions/base_update.html'
    slug_url_kwarg = 'product_slug'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse_lazy('companies:products:products', kwargs={'slug': self.kwargs.get('slug')})

    def get_context_data(self, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['previous'] = self.request.META.get('HTTP_REFERER')
        context['model_name'] = self.model.__name__
        return context


class ProductDeleteView(DeleteView):
    template_name = 'bases/actions/base_delete.html'
    slug_url_kwarg = 'product_slug'
    model = Product

    def get_success_url(self):
        return reverse_lazy('companies:products:products', kwargs={'slug': self.kwargs.get('slug')})

    def get_context_data(self, **kwargs):
        context = super(ProductDeleteView, self).get_context_data(**kwargs)
        context['previous'] = self.request.META.get('HTTP_REFERER')
        context['model_name'] = self.model.__name__
        return context
