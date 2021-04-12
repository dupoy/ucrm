from django import forms
from contacts.models import Contact


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
                choices=Contact.CONTACT_TYPE_CHOICES,
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
