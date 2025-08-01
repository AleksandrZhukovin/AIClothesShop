from django.contrib import admin
from server.apps.catalog.models import Item, ItemImage


__all__ = (
    "ItemAdmin",
    "ItemImageAdmin",
)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "color",
        "size",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "size",
    )


@admin.register(ItemImage)
class ItemImageAdmin(admin.ModelAdmin):
    list_display = (
        "item",
        "image",
    )
    list_filter = (
        "created_at",
        "updated_at",
    )
