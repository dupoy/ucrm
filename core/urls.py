from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from core.views import LandingView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('<slug:slug>/', include('companies.urls', namespace='companies')),
    path('', LandingView.as_view(), name='landing')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
