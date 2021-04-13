from django.urls import path

from managers.views import ManagerCreateView, ManagerUpdateView, ManagerDeleteView, ManagerListView

app_name = 'managers'

urlpatterns = [
    path('add/', ManagerCreateView.as_view(), name='add'),
    path('update/<int:pk>/', ManagerUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ManagerDeleteView.as_view(), name='delete'),
    path('', ManagerListView.as_view(), name='managers'),
]
