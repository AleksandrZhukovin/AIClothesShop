from django.db import models

from colorfield.fields import ColorField

from server.apps.core.models import TimeStampedMixin
from server.apps.catalog.choices import SizeChoices, FitChoices


class Item(TimeStampedMixin):
    category = models.ForeignKey(
        "catalog.Category", on_delete=models.CASCADE, related_name="items"
    )

    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    color = ColorField()
    size = models.CharField(max_length=10, choices=SizeChoices.choices)
    fit = models.CharField(max_length=10, choices=FitChoices.choices)

    def __str__(self):
        return f"Item | {self.name}"

    @classmethod
    def get_colors_by_category(cls, category_id):
        return (
            cls.objects.filter(category__pk=category_id)
            .values_list("color", flat=True)
            .distinct()
        )


class ItemImage(TimeStampedMixin):
    item = models.ForeignKey(
        "catalog.Item", on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="items/")

    def __str__(self):
        return f"Item image | {self.item.name}"


class ItemEditableImage(TimeStampedMixin):
    item = models.ForeignKey(
        "catalog.Item", on_delete=models.CASCADE, related_name="editable_images"
    )
    image = models.ImageField(upload_to="items/editables/")

    def __str__(self):
        return f"Item editable image | {self.item.name}"
