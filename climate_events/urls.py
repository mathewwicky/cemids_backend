from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClimateEventViewSet

router = DefaultRouter()
router.register(r'climate-events', ClimateEventViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
