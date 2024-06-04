from rest_framework import viewsets
from .serializers import EducationalContentSerializer
from .models import EducationalContent

class EducationalContentViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing educational content.
    """
    serializer_class = EducationalContentSerializer
    queryset = EducationalContent.objects.all()

   