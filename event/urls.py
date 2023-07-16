from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name = 'home_page'),
    path('add_event', views.add_event, name = 'add_event'),
    path('edit_event/<int:event_id>/',
         views.edit_event, name='edit_event'),
    
    ]