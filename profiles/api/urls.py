from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles.api.views import ProfileList, ProfileViewSet, ProfileStatusViewSet, AvatarUpdateView

router = DefaultRouter()
router.register(r"profilelist", ProfileViewSet)
router.register(r"status", ProfileStatusViewSet, basename="status")

urlpatterns = [
    path('profiles/', ProfileList.as_view(), name="profile-list"),
    path('', include(router.urls)),
    path('avatar/', AvatarUpdateView.as_view(), name="udpdate-avatar")

]