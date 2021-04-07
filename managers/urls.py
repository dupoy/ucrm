from django.urls import path

from managers.views import ManagerCreateView, ManagerUpdateView, ManagerDeleteView

app_name = 'managers'

urlpatterns = [
    path('add-manager/', ManagerCreateView.as_view(), name='add-manager'),
    path('<int:pk>/update-manager/', ManagerUpdateView.as_view(), name='update-manager'),
    path('<int:pk>/delete-manager/', ManagerDeleteView.as_view(), name='delete-manager'),
]
