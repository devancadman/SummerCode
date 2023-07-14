from django.shortcuts import render
from .models import UserProfile, Event

def home_page(request):

    events = Event.objects.all()
    context = {
        'events':events
    }
    return render(request, 'index.html', context)