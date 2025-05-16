from django.views.generic import ListView
from django.db.models import Prefetch

from server.apps.catalog.models import Item, ItemImage


__all__ = ('CategoryCatalogView',)


class CategoryCatalogView(ListView):
    model = Item
    context_object_name = 'categories'
    template_name = 'catalog/catalog_index.html'

    def get_queryset(self):
        return (
            Item.objects
            .prefetch_related(
                Prefetch('images', queryset=ItemImage.objects.only('image'))
            )
            .filter(category__pk=self.kwargs['category_id'])
        )
