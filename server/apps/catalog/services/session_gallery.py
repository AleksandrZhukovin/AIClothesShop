from server.apps.user.constants import SESSION_GALLERY_KEY
from server.apps.user.models import GalleryImage


class SessionGalleryManager:
    def __init__(self, session):
        self.session = session

    def add_image(self, file_url):
        gallery = self.session.setdefault(SESSION_GALLERY_KEY, [])
        gallery.append(file_url)
        self.session.modified = True

    def delete_image(self, file_url):
        self.session[SESSION_GALLERY_KEY].remove(file_url)
        GalleryImage.delete_image_from_media(file_url)

    def get_gallery(self):
        return self.session.setdefault(SESSION_GALLERY_KEY, [])
