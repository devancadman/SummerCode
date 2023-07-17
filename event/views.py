from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from .models import UserProfile, Event
from .forms import EventForm
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm

def home_page(request):

    events = Event.objects.all().order_by('-event_date')[:4]
    context = {
        'events':events
    }
    return render(request, 'index.html', context)

def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)

def add_event(request):
    """
    add_event.html
    """
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
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

from django.core.paginator import Paginator

def event_list(request):
    events = Event.objects.all()

    # Handling filter parameters
    location = request.GET.get('location')
    date = request.GET.get('date')

    if location:
        events = events.filter(event_location__icontains=location)

    if date:
        events = events.filter(event_date=date)

    # Applying pagination to filtered events
    paginator = Paginator(events, 3)  # Show 3 events per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'event_list.html', {'page_obj': page_obj})

def event_detail(request, event_id):
    # Your view logic goes here, and you can use the event_id parameter to fetch the specific event.
    return HttpResponse(f"This is the detail view for event {event_id}.")

from django.http import JsonResponse
from django.views.decorators.http import require_GET
from .models import Event

@require_GET
def api_filter_events(request):
    location = request.GET.get('location', '')
    date = request.GET.get('date', '')

    # Filter events based on the given criteria
    filtered_events = Event.objects.all()

    if location:
        filtered_events = filtered_events.filter(event_location__icontains=location)

    if date:
        filtered_events = filtered_events.filter(event_date=date)

    # You can add more filter criteria as needed

    # Serialize the events as JSON and return them
    data = [{'event_name': event.event_name, 'event_date': event.event_date.strftime('%Y-%m-%d'),
             'event_time': event.event_time.strftime('%H:%M:%S'), 'event_description': event.event_description,
             'event_location': event.event_location} for event in filtered_events]

    return JsonResponse(data, safe=False)

def event_map(request):
    return render(request, 'event_map.html')

def edit_event(request, event_id):

    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated event!')
            return redirect(reverse('home_page'))
        else:
            messages.error(
                request,
                'Failed to update event. Please ensure the form is valid.')
    else:
        form = EventForm(instance=event)
        messages.info(request, f'You are editing {event.event_name}')

    template = 'edit_event.html'
    context = {
        'form': form,
        'event': event,
    }

    return render(request, template, context)


def user_events(request):

    if request.user.is_authenticated:
        events = Event.objects.filter(organizer=request.user).order_by('-event_date')
        context = {
        'events':events
    }
    return render(request, 'user_events.html', context)