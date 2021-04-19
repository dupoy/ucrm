from django import forms
from contacts.models import Contact, ContactType, ContactHistory
from core.forms import DateTimePicker


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['avatar', 'customer']
        labels = {
            'type': 'Contact type',
            'value': 'Contact'
        }
        widgets = {
            'type': forms.Select(
                choices=ContactType.choices,
                attrs={
                    'id': 'type-id',
                    'class': 'form-control',

                }
            ),
            'value': forms.TextInput(
                attrs={
                    'id': 'value-id',
                    'class': 'form-control',
                }
            ),
        }


class ContactHistoryForm(forms.ModelForm):
    class Meta:
        model = ContactHistory
        exclude = ['manager']
        labels = {
            'contact': 'Contact',
            'date': 'Contact date'
        }
        widgets = {
            'contact': forms.Select(
                attrs={
                    'id': 'type-id',
                    'class': 'form-control',

                }
            ),
            'date': DateTimePicker(
                attrs={
                    'id': 'datetime-id',
                    'class': 'form-control',
                }
            ),
        }
