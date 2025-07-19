from django.contrib import admin
from server.apps.catalog.models import Item, ItemImage


admin.site.register(Item)
admin.site.register(ItemImage)
