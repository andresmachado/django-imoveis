from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from smart_selects.db_fields import ChainedForeignKey


class PropertyType(models.Model):
    name = models.CharField(max_length=140)

    class Meta:
        verbose_name = _("Tipo do imóvel")
        verbose_name_plural = _('Tipos de imóveis')

    def __str__(self):
        return self.name

class Category(models.Model):
    title = models.CharField(max_length=140)
    property_type = models.ForeignKey(PropertyType)

    class Meta:
        verbose_name = _("Categoria")
        verbose_name_plural = _('Categorias')

    def __str__(self):
        return self.title

class Property(models.Model):

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    help_text =_("Utilize este espaço para descrever seu anúncio. Quanto mais detalhado, maiores serão as chances de conseguir um bom negócio.")
    cep = models.CharField(max_length=8, default='')
    address = models.CharField(max_length=140)
    state = models.CharField(max_length=140)
    city = models.CharField(max_length=140)
    district = models.CharField(max_length=140)
    property_type = models.ForeignKey(PropertyType)
    category = ChainedForeignKey(Category, chained_field='property_type', chained_model_field='property_type')
    rooms = models.PositiveSmallIntegerField()
    util_area = models.PositiveSmallIntegerField(blank=True, null=True)
    total_area = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=140)
    image = models.ImageField(upload_to='img/')
    description = models.TextField()
    rent_price = models.DecimalField(max_digits=19, decimal_places=10)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Imóvel")
        verbose_name_plural = _('Imóveis')

    def __str__(self):
        return self.title
