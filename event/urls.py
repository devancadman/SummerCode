from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('add_event', views.add_event, name = 'add_event'),
    path('edit_event/<int:event_id>/', views.edit_event, name = 'edit_event'),
    path('contact', views.contact, name= 'contact'),
    path('user_events', views.user_events, name= 'user_events'),
    path('events/', views.event_list, name='event_list'),
    path('api/events/', views.api_filter_events, name='api_filter_events'),  # URL for the Ajax view
    path('events/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event_map/', views.event_map, name='event_map'),
]
