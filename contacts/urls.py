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
    path('add/', ContactCreateView.as_view(), name='add'),
    path('update/<int:pk_contact>/', ContactUpdateView.as_view(), name='update'),
    path('delete/<int:pk_contact>/', ContactDeleteView.as_view(), name='delete'),

    path('add-history/', ContactHistoryCreate.as_view(), name='add-history'),
    path('update-history/<int:pk_contact_history>/', ContactHistoryUpdate.as_view(), name='update-history'),
    path('delete-history/<int:pk_contact_history>/', ContactHistoryDelete.as_view(), name='delete-history'),
]
