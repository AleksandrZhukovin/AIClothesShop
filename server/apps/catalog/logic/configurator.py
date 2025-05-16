from django.views.generic import DetailView

from server.apps.catalog.models import Category


__all__ = ('ConfiguratorView',)


class ConfiguratorView(DetailView):
    pass
