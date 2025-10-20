from django.views.generic import ListView, DeleteView, View
from django.http import HttpResponse

from server.apps.user.models import GalleryImage
from server.apps.catalog.services.session_gallery import SessionGalleryManager


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
        return SessionGalleryManager(self.request.session).get_gallery()


class GalleryImageDeleteView(DeleteView):
    model = GalleryImage
    pk_url_kwarg = "image_id"

    def form_valid(self, form):
        self.object.delete()
        return HttpResponse()


class SessionGalleryImageDeleteView(View):
    def post(self, request, *args, **kwargs):
        image_url = self.request.POST.get("image_url")
        # GalleryImage.unauthenticated_user_delete(self.request.session, image_url)
        return HttpResponse()
