from django.urls import path

from server.apps.user.logic.profile import *
from server.apps.user.logic.gallery import *

app_name = "user"

urlpatterns = [
    path("profile/<int:profile_id>/", UserProfileView.as_view(), name="user_profile"),
    path(
        "auth/gallery/",
        UserGalleryView.as_view(),
        name="auth_user_gallery",
    ),
    path(
        "gallery/",
        SessionGalleryView.as_view(),
        name="session_user_gallery",
    ),
    path(
        "gallery/image/<int:image_id>/delete/",
        GalleryImageDeleteView.as_view(),
        name="gallery_image_delete",
    ),
]
