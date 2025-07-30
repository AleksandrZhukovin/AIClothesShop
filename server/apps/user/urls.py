from django.urls import path

from server.apps.user.logic.profile import *

app_name = "user"

urlpatterns = [
    path("profile/<int:profile_id>/", UserProfileView.as_view(), name="user_profile"),
    path(
        "profile/user/<int:user_id>/gallary/",
        UserGallaryView.as_view(),
        name="user_gallary",
    ),
]
