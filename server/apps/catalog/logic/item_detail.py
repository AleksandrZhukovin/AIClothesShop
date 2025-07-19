from django.views.generic import DetailView

from server.apps.catalog.models import Item


__all__ = ("ItemDetailView",)


class ItemDetailView(DetailView):
    model = Item
    template_name = "catalog/item_detail.html"
    context_object_name = "item"
    slug_url_kwarg = "item_id"
    slug_field = "id"
