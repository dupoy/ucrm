from django.urls import path

from contacts.views import (
    ContactDeleteView,
    ContactCreateView,
)

app_name = 'contacts'

urlpatterns = [
    path('<int:pk>/add', ContactCreateView.as_view(), name='add'),
    path('<int:id>:<int:pk>/delete', ContactDeleteView.as_view(), name='delete'),
]
