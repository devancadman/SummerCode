"forms.py"

from .models import UserProfile, Event
from django import forms
from .widgets import  DatePickerInput, TimePickerInput
import datetime
from django.core.exceptions import ValidationError
from .models import Event, UserProfile


class UserProfileForm(forms.ModelForm):
    "User profile form"

    model = UserProfile()
    exclude = ('user',)


class EventForm(forms.ModelForm):
    "Event form"
    class Meta:
        """ fields for recipe form"""
        model = Event
        fields = ('event_name', 'event_date', 'event_time','event_image', 'event_description',
                  'event_location')

        labels = {
            'event_name' : 'Event Name',
            'event_date': 'Event Date',
            'event_time': 'Event Time',
            'event_image': 'Event Image',
            'event_description': 'Description',
            'event_location': 'Event Location'
        }


        widgets = {
            'event_date' : DatePickerInput(),
            'event_time' : TimePickerInput(),
        }