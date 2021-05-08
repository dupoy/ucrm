import re

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import resolve

from companies.models import Company


class PreviousPageMixin:
    def get_context_data(self, **kwargs):
        if 'previous' not in kwargs:
            kwargs['previous'] = self.request.META.get('HTTP_REFERER')
        return super().get_context_data(**kwargs)


class ModelNameMixin:
    def get_context_data(self, **kwargs):
        if 'model_name' not in kwargs:
            model_name = ' '.join(re.findall('[A-Z][^A-Z]*', self.model.__name__))
            kwargs['model_name'] = model_name
        return super().get_context_data(**kwargs)


class LinkMixin:
    def get_context_data(self, **kwargs):
        if 'current_url' not in kwargs:
            kwargs['current_url'] = resolve(self.request.path_info).app_names[-1]
        if 'company' not in kwargs:
            if 'slug' in self.kwargs:
                kwargs['company'] = Company.objects.get(slug=self.kwargs.get('slug'))
        return super().get_context_data(**kwargs)


class PermissionMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_director:
            return redirect('accounts:profile')
        return super().dispatch(request, *args, **kwargs)
