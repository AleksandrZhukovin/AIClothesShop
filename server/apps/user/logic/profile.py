from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from server.apps.user.models import Profile


__all__ = ("UserProfileView",)


class UserProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = "user/profile.html"
    context_object_name = "profile"

    def get_queryset(self):
        return Profile.objects.select_related("user")

    def get_object(self, queryset=None):
        return Profile.objects.select_related("user").get(
            pk=self.request.user.profile.pk
        )
