from django.db import models
from django.utils.translation import gettext_lazy as _


class CategoryChoices(models.TextChoices):
    TSHIRT = 'tshirt', _('T-Shirt')
    SHIRT = 'shirt', _('Shirt')
    HOODIE = 'hoodie', _('Hoodie')


class SizeChoices(models.TextChoices):
    XS = 'XS', _('XS')
    S = 'S', _('S')
    M = 'M', _('M')
    L = 'L', _('L')
    XL = 'XL', _('XL')
    XXL = 'XXL', _('XXL')
    XXXL = 'XXXL', _('XXXL')


class FitChoices(models.TextChoices):
    SLIM = 'slim', _('Slim')
    STANDARD = 'standard', _('Standard')
    LOOSE = 'loose', _('Loose')
    OVERSIZE = 'oversize', _('Oversize')
