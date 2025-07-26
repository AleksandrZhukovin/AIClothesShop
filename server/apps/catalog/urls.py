from django.urls import path

from server.apps.catalog.logic.catalog_index import *
from server.apps.catalog.logic.category_items import *
from server.apps.catalog.logic.configurator import *
from server.apps.catalog.logic.item_detail import *

app_name = "catalog"

urlpatterns = [
    path("", CatalogIndexView.as_view(), name="index"),
    path(
        "category/<int:category_id>/catalog/",
        CategoryCatalogView.as_view(),
        name="category-catalog",
    ),
    path("item/<int:item_id>/", ItemDetailView.as_view(), name="item-detail"),
    path(
        "item/<int:item_id>/configurator/",
        ConfiguratorView.as_view(),
        name="item-configurator",
    ),
]
