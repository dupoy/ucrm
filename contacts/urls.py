from django.urls import path

from contacts.views import (
    ContactDeleteView,
    ContactCreateView,
    ContactUpdateView,
    ContactHistoryCreate,
    ContactHistoryDelete,
    ContactHistoryUpdate
)

app_name = 'contacts'

urlpatterns = [
    path('<int:pk>/add', ContactCreateView.as_view(), name='add'),
    path('<int:id>/<int:pk>/update', ContactUpdateView.as_view(), name='update'),
    path('<int:id>/<int:pk>/delete', ContactDeleteView.as_view(), name='delete'),

    path('<int:pk>/add-history', ContactHistoryCreate.as_view(), name='add-history'),
    path('<int:id>/<int:pk>/update-history', ContactHistoryUpdate.as_view(), name='update-history'),
    path('<int:id>/<int:pk>/delete-history', ContactHistoryDelete.as_view(), name='delete-history'),
]
