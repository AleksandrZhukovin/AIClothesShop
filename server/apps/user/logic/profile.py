from django.db.models.base import Model as Model
from server.apps.user.models import Profile, GallaryImage
from django.views.generic import DetailView, ListView


__all__ = (
    "UserProfileView",
    "UserGallaryView",
)


class UserProfileView(DetailView):
    model = Profile
    template_name = "user/profile.html"
    pk_url_kwarg = "profile_id"

    def get_queryset(self):
        return super().get_queryset().select_related("user")


class UserGallaryView(ListView):
    model = GallaryImage
    template_name = "user/partials/gallary.html"
    context_object_name = "gallary"

    def get_queryset(self):
        return super().get_queryset().filter(user__pk=self.kwargs["user_id"])
