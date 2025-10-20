from server.apps.user.constants import SESSION_GALLERY_KEY
from server.apps.user.models import GalleryImage


class SessionGalleryManager:
    @staticmethod
    def add_image(session, file_url):
        gallery = session.setdefault(SESSION_GALLERY_KEY, [])
        gallery.append(file_url)
        session.modified = True

    @staticmethod
    def delete_image(session, file_url):
        session[SESSION_GALLERY_KEY].remove(file_url)
        GalleryImage.delete_image_from_media(file_url)
