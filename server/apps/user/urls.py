from django.urls import path

from server.apps.user.logic.profile import *
from server.apps.user.logic.gallery import *
from server.apps.user.constants import AUTHENTICATED_USER_GALLERY, SESSION_USER_GALLERY

app_name = "user"

urlpatterns = [
    path("profile/<int:profile_id>/", UserProfileView.as_view(), name="user_profile"),
    path(
        "auth/gallery/",
        GalleryView.as_view(gallery_type=AUTHENTICATED_USER_GALLERY),
        name="auth_user_gallery",
    ),
    path(
        "gallery/",
        GalleryView.as_view(gallery_type=SESSION_USER_GALLERY),
        name="session_user_gallery",
    ),
    path(
        "gallery/image/<int:image_id>/delete/",
        GalleryImageDeleteView.as_view(),
        name="gallery_image_delete",
    ),
]
