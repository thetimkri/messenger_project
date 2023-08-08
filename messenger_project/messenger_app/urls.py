from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, MessageViewSet

router = DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
