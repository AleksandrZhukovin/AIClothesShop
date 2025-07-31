import base64
import uuid

from django.db import models
from django.contrib.auth import get_user_model
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

from server.apps.user.constants import SESSION_GALLERY_KEY


class GalleryImage(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="gallery_images/")

    @staticmethod
    def unauthenticated_user_save(image_data, session) -> str | None:
        if not isinstance(image_data, (list, tuple)) or not image_data:
            return None

        file_url = GalleryImage.save_image_to_media(image_data)

        GalleryImage.get_session_gallery(session)
        session[SESSION_GALLERY_KEY].append(file_url)
        session.modified = True

        return file_url

    @staticmethod
    def get_session_gallery(session) -> list[str]:
        return session.setdefault(SESSION_GALLERY_KEY, [])

    @staticmethod
    def save_image_to_media(image_data) -> str:
        image_base64 = image_data[0]
        image_bytes = base64.b64decode(image_base64)
        filename = f"temp/{uuid.uuid4().hex}.png"
        file_path = default_storage.save(filename, ContentFile(image_bytes))
        return f"/media/{file_path}"
