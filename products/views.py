from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from companies.models import Company
from core.mixins import PreviousPageMixin, ModelNameMixin, LinkMixin
from products.forms import ProductForm
from products.models import Product


class ProductListView(LoginRequiredMixin, LinkMixin, ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    model = Product

    def get_queryset(self):
        return Product.objects.filter(company__slug=self.kwargs.get('slug'))


class ProductCreateView(LoginRequiredMixin, ModelNameMixin, PreviousPageMixin, CreateView):
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

    def get_queryset(self):
        return Company.objects.get(slug=self.kwargs['slug']).products.all()


class ProductUpdateView(LoginRequiredMixin, PreviousPageMixin, UpdateView):
    template_name = 'bases/actions/base_update.html'
    slug_url_kwarg = 'product_slug'
    form_class = ProductForm
    model = Product

    def get_success_url(self):
        return reverse_lazy('companies:products:products', kwargs={'slug': self.kwargs.get('slug')})


class ProductDeleteView(LoginRequiredMixin, PreviousPageMixin, DeleteView):
    template_name = 'bases/actions/base_delete.html'
    slug_url_kwarg = 'product_slug'
    model = Product

    def get_success_url(self):
        return reverse_lazy('companies:products:products', kwargs={'slug': self.kwargs.get('slug')})
