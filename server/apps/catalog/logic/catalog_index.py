from django.views.generic import ListView

from server.apps.catalog.models import Category


__all__ = ('CatalogIndexView',)


class CatalogIndexView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'catalog/catalog_index.html'
