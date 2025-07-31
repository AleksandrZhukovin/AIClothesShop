from django.db.models.base import Model as Model
from server.apps.user.models import Profile
from django.views.generic import DetailView


__all__ = ("UserProfileView",)


class UserProfileView(DetailView):
    model = Profile
    template_name = "user/profile.html"
    pk_url_kwarg = "profile_id"

    def get_queryset(self):
        return super().get_queryset().select_related("user")
