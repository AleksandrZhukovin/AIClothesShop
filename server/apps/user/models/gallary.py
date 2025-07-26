from django.db import models
from django.contrib.auth import get_user_model
import base64
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


class GallaryImage(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="images"
    )

    image = models.ImageField(upload_to="gallary_images/")

    @staticmethod
    def unauthenticated_user_save(image_data, response):
        if image_data:
            image_base64 = image_data[0]
            image_bytes = base64.b64decode(image_base64)
            filename = f"temp/{response.id}.png"
            file_path = default_storage.save(filename, ContentFile(image_bytes))
            return f"/media/{file_path}"
