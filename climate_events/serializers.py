from rest_framework import serializers
from .models import ClimateEvent

class ClimateEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClimateEvent
        fields = ['event_title', 'event_description', 'location', 'date', 'time', 'image']
