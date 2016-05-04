from django.db import models
from django.utils.translation import ugettext_lazy as _

class Property(models.Model):
    ## Choices for property category
    CATEGORY_STANDARD = 1
    CATEGORY_DUPLEX = 2
    CATEGORY_TRIPLEX = 3
    CATEGORY_PENTHOUSE = 4
    CATEGORY_DUPLEX_PENTHOUSE = 5
    CATEGORY_TRIPLEX_PENTHOUSE = 6

    CATEGORY_CHOICES = (
        (CATEGORY_STANDARD, _('Padrão')),
        (CATEGORY_DUPLEX, _('Duplex')),
        (CATEGORY_TRIPLEX, _('Triplex')),
        (CATEGORY_PENTHOUSE, _('Cobertura')),
        (CATEGORY_DUPLEX_PENTHOUSE, _('Cobertura Duplex')),
        (CATEGORY_TRIPLEX_PENTHOUSE, _('Cobetura Triplex'))
    )

    ## Choices for property type
    TYPE_APARTMENT = 1
    TYPE_HOUSE = 2

    TYPE_CHOICES = (
        (TYPE_APARTMENT, _('Apartamentos')),
        (TYPE_HOUSE, _('Casas'))
    )

    help_text =_("Utilize este espaço para descrever seu anúncio. Quanto mais detalhado, maiores serão as chances de conseguir um bom negócio.")
    property_type = models.CharField(choices=TYPE_CHOICES, default=TYPE_APARTMENT)
    category = models.CharField(choices = CATEGORY_CHOICES, default=CATEGORY_STANDARD)
    rooms = models.PositiveSmallIntegerField()
    util_area = models.PositiveSmallIntegerField()
    total_area = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=140)
    description = models.TextField()
    rent_price = models.DecimalField(max_digits=19, decimal_places=10)
    image = models.ImageField(upload_to='static/img/')
    timestamp = models.DateTimeField(auto_now=True)