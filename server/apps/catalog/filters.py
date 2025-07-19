import django_filters
from django.utils.translation import gettext_lazy as _

from server.apps.catalog.models import Item
from server.apps.catalog.choices import SizeChoices, FitChoices


class ItemFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr="lte")

    size = django_filters.ChoiceFilter(
        choices=SizeChoices.choices, empty_label=_("All Sizes")
    )
    fit = django_filters.ChoiceFilter(
        choices=FitChoices.choices, empty_label=_("All Fits")
    )
    color = django_filters.CharFilter(method="filter_colors")

    class Meta:
        model = Item
        fields = ["size", "fit", "color"]

    def filter_colors(self, queryset, name, value):
        if not value:
            return queryset
        colors = self.data.getlist("color")
        if colors:
            return queryset.filter(color__in=colors)
        return queryset
