from django.db import models
from django.utils.translation import gettext_lazy as _


class CategoryChoices(models.TextChoices):
    TSHIRT = 'tshirt', _('T-Shirt')
    SHIRT = 'shirt', _('Shirt')
    HOODIE = 'hoodie', _('Hoodie')
