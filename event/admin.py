from django.contrib import admin
from .models import UserProfile, Event

@admin.register(UserProfile)
class AdminUserProfile(admin.ModelAdmin):
    """
    User profile class in admin panel
    """
    list_display = ('user', 'contact_info', 'user_description')


@admin.register(Event)
class AdminEvent(admin.ModelAdmin):
    """
    User profile class in admin panel
    """
    list_display = ('organizer', 'event_name', 'event_date_time')
    
