from django.db.models.base import Model as Model
from django.views.generic import ListView

from server.apps.user.models import GalleryImage
from server.apps.user.constants import AUTHENTICATED_USER_GALLERY, SESSION_USER_GALLERY


__all__ = ("UserGalleryView",)


class UserGalleryView(ListView):
    model = GalleryImage
    context_object_name = "gallery"
    gallery_type = None

    def get_queryset(self):
        if self.gallery_type == AUTHENTICATED_USER_GALLERY:
            return super().get_queryset().filter(user__pk=self.request.user.id)
        elif self.gallery_type == SESSION_USER_GALLERY:
            return GalleryImage.get_session_gallery(self.request.session)

    def get_template_names(self):
        if self.gallery_type == AUTHENTICATED_USER_GALLERY:
            return "user/partials/auth_user_gallery.html"
        elif self.gallery_type == SESSION_USER_GALLERY:
            return "user/partials/session_gallery.html"
