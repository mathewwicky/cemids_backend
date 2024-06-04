from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EducationalContentViewSet

router = DefaultRouter()
router.register(r'educational-content', EducationalContentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
