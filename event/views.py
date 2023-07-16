from django.shortcuts import render, redirect, reverse
from .models import UserProfile, Event
from .forms import EventForm
from django.contrib import messages

def home_page(request):

    events = Event.objects.all()
    context = {
        'events':events
    }
    return render(request, 'index.html', context)


def add_event(request):
    """
    add_event.html
    """
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            messages.success(request, 'Event Created!')
            return redirect(reverse('home_page'))
        else:
            messages.error(request, 'Failed to create an event.\
                Please ensure that form is valid.')
    else:
        form = EventForm()

    template = 'add_event.html'
    context = {
        'form':form,
     }
    return render(request, template, context)


