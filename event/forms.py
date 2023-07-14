"forms.py"

from django import forms
from .models import UserProfile, Event

class UserProfileForm(forms.ModelForm):
    "User profile form"

    model = UserProfile()
    exclude = ('user',)


class EventForm(forms.ModelForm):
    "Event form"

    model = Event()