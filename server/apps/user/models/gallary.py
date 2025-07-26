from django.db import models
from django.contrib.auth import get_user_model


class Gallary(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE, related_name="gallary"
    )


class GallaryImage(models.Model):
    gallary = models.ForeignKey(
        "user.Gallary", on_delete=models.CASCADE, related_name="images"
    )

    image = models.ImageField(upload_to="gallary_images/")
