from render_block import render_block
from django_filters.views import FilterView

from django.views.generic import ListView
from django.db.models import Prefetch

from server.apps.catalog.models import Item, ItemImage
from server.apps.catalog.filters import ItemFilter


__all__ = ("CategoryCatalogView",)


class CategoryCatalogView(FilterView, ListView):
    model = Item
    context_object_name = "items"
    template_name = "catalog/catalog_items.html"
    filterset_class = ItemFilter

    def get_queryset(self):
        return Item.objects.prefetch_related(
            Prefetch("images", queryset=ItemImage.objects.only("image"))
        ).filter(category__pk=self.kwargs["category_id"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["available_colors"] = Item.get_colors_by_category(
            self.kwargs["category_id"]
        )
        return context

    def get(self, request, *args, **kwargs):
        if self.request.htmx:
            filterset_class = self.get_filterset_class()
            self.filterset = self.get_filterset(filterset_class)

            if (
                not self.filterset.is_bound
                or self.filterset.is_valid()
                or not self.get_strict()
            ):
                self.object_list = self.filterset.qs
            else:
                self.object_list = self.filterset.queryset.none()

            context = self.get_context_data(
                filter=self.filterset, object_list=self.object_list
            )
            return render_block(request, self.template_name, "catalog_items", context)
        return super().get(request, *args, **kwargs)
