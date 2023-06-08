from rest_framework import serializers

from events.models import Event

class EventSerializer(serializers.ModelSerializer):
    attendees = serializers.SerializerMethodField
    class Meta:
        model = Event
        fields = '__all__'
