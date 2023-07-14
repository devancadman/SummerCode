from django.db import models

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
    event_name = models.CharField(max_length=80,null=False, blank=False)
    event_date_time = models.DateTimeField()
    event_description = models.TextField()
    event_location = models.CharField(max_length=80, null=False, blank=False)