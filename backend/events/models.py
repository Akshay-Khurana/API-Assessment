from django.db import models
from django.conf import settings

from events import constants as event_constants
# Create your models here.
class Event(models.Model):
    """
    """
    type = models.CharField(max_length=10, default="event")
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    schedule = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="events/images/")
    moderator = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='moderator_event'
    )
    category = models.IntegerField(choices=event_constants.CATEGORY_CHOICES)
    sub_category = models.IntegerField(choices=event_constants.SUB_CATEGORY_CHOICES)
    rigor_rank = models.IntegerField(default=0)
    attendees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='attendees_event', blank=True)
