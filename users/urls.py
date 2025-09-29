from django.urls import path, include
from rest_framework import routers

from users.api_views import ProfileView, RidersListView
from users.views import UserViewSet, PassengerViewSet, RiderViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'passengers', PassengerViewSet, basename='passenger')
router.register(r'riders', RiderViewSet, basename='rider')

urlpatterns = [
    path("profile/", ProfileView.as_view(), name="profile"),
    path("riders/", RidersListView.as_view(), name="riders-list"),
]