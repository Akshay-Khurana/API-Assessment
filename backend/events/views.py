from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from events.serializers import Event, EventSerializer


# Create your views here.
class EventAPIViewset(ModelViewSet):
    """
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
