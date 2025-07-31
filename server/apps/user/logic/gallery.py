from django.db.models.base import Model as Model
from server.apps.user.models import GalleryImage
from server.apps.user.constants import AUTHENTICATED_USER_GALLERY, SESSION_USER_GALLERY
from django.views.generic import DetailView, ListView


__all__ = ("UserGalleryView",)


class UserGalleryView(ListView):
    model = GalleryImage
    template_name = "user/partials/gallery.html"
    context_object_name = "gallery"
    gallery_type = None

    def get_queryset(self):
        if self.gallery_type == AUTHENTICATED_USER_GALLERY:
            return super().get_queryset().filter(user__pk=self.kwargs["user_id"])
        elif self.gallery_type == SESSION_USER_GALLERY:
            pass
