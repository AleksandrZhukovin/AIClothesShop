from django.db import models

from server.apps.core.models import TimeStampedMixin


class Item(TimeStampedMixin):
    category = models.ForeignKey('catalog.Category', on_delete=models.CASCADE, related_name='items')

    name = models.CharField(max_length=100)
    # Price will vary depending on print
    price_start = models.DecimalField(max_digits=5, decimal_places=2)
    price_finish = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Item | {self.name}"


class ItemImage(models.Model):
    item = models.ForeignKey('catalog.Item', on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="items/")

    def __str__(self):
        return f"Item image | {self.item.name}"
