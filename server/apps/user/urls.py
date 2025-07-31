from django.urls import path

from server.apps.user.logic.profile import *
from server.apps.user.logic.gallery import *
from server.apps.user.constants import AUTHENTICATED_USER_GALLERY, SESSION_USER_GALLERY

app_name = "user"

urlpatterns = [
    path("profile/<int:profile_id>/", UserProfileView.as_view(), name="user_profile"),
    path(
        "<int:user_id>/gallery/",
        UserGalleryView.as_view(gallery_type=AUTHENTICATED_USER_GALLERY),
        name="auth_user_gallery",
    ),
    path(
        "gallery/",
        UserGalleryView.as_view(gallery_type=SESSION_USER_GALLERY),
        name="session_user_gallery",
    ),
]
