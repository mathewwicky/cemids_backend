from rest_framework import serializers
from .models import EducationalContent

class EducationalContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalContent
        fields = '__all__'  # Include all fields by default (adjust as needed)
