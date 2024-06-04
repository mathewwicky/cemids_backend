from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClimateEventSerializer
from .models import ClimateEvent

# Create your views here.

class ClimateEventViewSet(viewsets.ModelViewSet):
    serializer_class = ClimateEventSerializer
    queryset = ClimateEvent.objects.all()
