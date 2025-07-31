from django.contrib import admin
from server.apps.user.models import Profile, GalleryImage


admin.site.register(Profile)
admin.site.register(GalleryImage)
