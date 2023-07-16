from django.db import models
import datetime
from django.core.exceptions import ValidationError

# Create your models here.
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=13, null=False, blank=False)
    user_description = models.TextField()

    def __str__(self):
        return self.user.username


class Event(models.Model):
    organizer = models.ForeignKey(User, on_delete=models.CASCADE,related_name='event_posts') 
    event_name = models.CharField(max_length=80, null=False, blank=False)
    event_date = models.DateField( null=False, blank=False)
    event_time = models.TimeField( null=False, blank=False)
    event_description = models.TextField(null=True)
    event_location = models.CharField(max_length=80, null=False, blank=False)

    def __str__(self):
        return self.event_name
