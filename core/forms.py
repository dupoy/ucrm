from django.forms.widgets import Input


class DateTimePicker(Input):
    input_type = 'datetime-local'