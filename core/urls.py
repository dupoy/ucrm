from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from core.views import LandingView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('contacts/', include('contacts.urls', namespace='contacts')),
    path('<slug:slug>/', include('companies.urls', namespace='companies')),
    path('<slug:company_slug>/managers/', include('managers.urls', namespace='managers')),
    path('<slug:company_slug>/products/', include('products.urls', namespace='products')),
    path('<slug:company_slug>/customers/', include('customers.urls', namespace='customers')),
    path('', LandingView.as_view(), name='landing')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
