from django.urls import path

from managers.views import ManagerCreateView, ManagerUpdateView, ManagerDeleteView, ManagerListView

app_name = 'managers'

urlpatterns = [
    path('add/', ManagerCreateView.as_view(), name='add'),
    path('<int:pk>/update/', ManagerUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', ManagerDeleteView.as_view(), name='delete'),
    path('<slug:slug>/', ManagerListView.as_view(), name='managers'),
]
