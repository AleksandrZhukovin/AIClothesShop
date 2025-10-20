from django.core.files.base import ContentFile

from server.apps.catalog.services.session_gallery import SessionGalleryManager
from server.apps.user.models import GalleryImage


class UserGalleryManager:
    def __init__(self, user, session=None):
        self.user = user
        self.session = session

    def authenticated_user_save_image(self, image: ContentFile) -> str:
        gallery_image = GalleryImage.objects.create(user=self.user, image=image)
        return gallery_image.url

    def unauthenticated_user_save_image(self, image: ContentFile) -> str:
        if not self.session:
            raise ValueError("Session required for an unauthenticated user.")
        image_url = GalleryImage.save_image_to_media(image)

        session_gallery_manager = SessionGalleryManager(self.session)
        session_gallery_manager.add_image(image_url)
        return image_url

    def save_image(self, image: ContentFile) -> str:
        if self.user.is_authenticated:
            image_url = self.authenticated_user_save_image(image)
        else:
            image_url = self.unauthenticated_user_save_image(image)
        return image_url
