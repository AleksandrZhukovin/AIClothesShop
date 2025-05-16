from django.urls import path
from django.views.decorators.cache import cache_page

from server.apps.catalog.logic.catalog_index import *
from server.apps.catalog.logic.configurator import *


app_name = 'catalog'

urlpatterns = [
    path('', cache_page(60 * 15)(CatalogIndexView.as_view()), name='index'),
    path('', ConfiguratorView.as_view(), name='configurator'),
]
