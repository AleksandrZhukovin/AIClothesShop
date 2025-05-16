from django.db import models

from server.apps.core.models import TimeStampedMixin
from server.apps.catalog.choices import CategoryChoices


class Category(TimeStampedMixin):
    name = models.CharField(max_length=100, choices=CategoryChoices.choices)

    def __str__(self):
        return f"Category | {self.get_name_display()}"
    

class CategoryImage(models.Model):
    category = models.ForeignKey('catalog.Category', on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="categories/")

    def __str__(self):
        return f"Category image | {self.category.name}"
    