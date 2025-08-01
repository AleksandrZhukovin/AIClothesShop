from django.views.generic import ListView, DeleteView
from django.http import HttpResponse

from server.apps.user.models import GalleryImage


__all__ = ("UserGalleryView", "SessionGalleryView", "GalleryImageDeleteView")


class AbstractGalleryView(ListView):
    model = GalleryImage
    context_object_name = "gallery"


class UserGalleryView(AbstractGalleryView):
    template_name = "user/partials/auth_user_gallery.html"

    def get_queryset(self):
        return super().get_queryset().filter(user__pk=self.request.user.id)


class SessionGalleryView(AbstractGalleryView):
    template_name = "user/partials/session_gallery.html"

    def get_queryset(self):
        return self.model.get_session_gallery(self.request.session)


class GalleryImageDeleteView(DeleteView):
    model = GalleryImage
    pk_url_kwarg = "image_id"

    def form_valid(self, form):
        self.object.delete()
        return HttpResponse()
