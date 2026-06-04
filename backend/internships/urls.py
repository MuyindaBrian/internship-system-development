from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InternshipViewSet, InternshipApplicationViewSet

router = DefaultRouter()
router.register(r'internships', InternshipViewSet, basename='internship')
router.register(r'applications', InternshipApplicationViewSet, basename='application')

urlpatterns = [
    path('', include(router.urls)),
]
