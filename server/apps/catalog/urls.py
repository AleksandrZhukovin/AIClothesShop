from django.urls import path

from server.apps.catalog.logic.catalog_index import *
from server.apps.catalog.logic.category_items import *
from server.apps.catalog.logic.configurator import *


app_name = 'catalog'

urlpatterns = [
    path('', CatalogIndexView.as_view(), name='index'),
    path('configurator/', ConfiguratorView.as_view(), name='configurator'),
    path('category/<int:category_id>/catalog/', CategoryCatalogView.as_view(), name='category-catalog'),
]
