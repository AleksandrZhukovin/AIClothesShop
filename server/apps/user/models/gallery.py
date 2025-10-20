import os
import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


class GalleryImage(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="gallery_images/")

    @staticmethod
    def save_image_to_media(image: ContentFile) -> str:
        filename = f"temp/{uuid.uuid4().hex}.png"
        file_path = default_storage.save(filename, image)
        return default_storage.url(file_path)

    @staticmethod
    def delete_image_from_media(image_url):
        path = image_url.replace(f"{default_storage.url('')}", "")

        if default_storage.exists(path):
            default_storage.delete(path)
