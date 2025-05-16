from django.contrib import admin

from server.apps.catalog.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('created_at', 'updated_at',)
