from django.views.generic import ListView, DeleteView, View
from django.http import HttpResponse

from server.apps.user.models import GalleryImage
from server.apps.catalog.services.session_gallery import SessionGalleryManager


__all__ = (
    "UserGalleryView",
    "SessionGalleryView",
    "GalleryImageDeleteView",
    "SessionGalleryImageDeleteView",
)


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
        return SessionGalleryManager(self.request.session).get_gallery()


class GalleryImageDeleteView(DeleteView):
    model = GalleryImage
    pk_url_kwarg = "image_id"

    def form_valid(self, form):
        self.object.delete()
        return HttpResponse()


class SessionGalleryImageDeleteView(View):
    def post(self, request, *args, **kwargs):
        session_gallery_manager = SessionGalleryManager(self.request.session)
        session_gallery_manager.delete_image(self.kwargs["image_key"])
        return HttpResponse()
