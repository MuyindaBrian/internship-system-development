from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AOBRequestViewSet

router = DefaultRouter()
router.register(r'aob', AOBRequestViewSet, basename='aob')

urlpatterns = [
    path('', include(router.urls)),
]
