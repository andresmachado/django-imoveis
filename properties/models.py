from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from smart_selects.db_fields import ChainedForeignKey


class PropertyType(models.Model):
    """Class that implements properties types, as House or Apartment."""

    name = models.CharField(_('Tipo do imóvel'), max_length=140)

    class Meta:
        """Set configurations for the PropertyType model."""

        verbose_name = _("Tipo do imóvel")
        verbose_name_plural = _('Tipos de imóveis')

    def __str__(self):
        return self.name


class Category(models.Model):
    """Model for category of properties."""

    title = models.CharField(_('Categoria'), max_length=140)
    property_type = models.ForeignKey(PropertyType)

    class Meta:
        """Set configurations for the Category model."""

        verbose_name = _("Categoria")
        verbose_name_plural = _('Categorias')

    def __str__(self):
        return self.title


class Property(models.Model):
    """Model for all properties."""

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    help_text = _("Utilize este espaço para descrever seu anúncio.")
    cep = models.CharField(max_length=8, default='')
    address = models.CharField(_('Endereço'), max_length=140)
    state = models.CharField(_('Estado'), max_length=2)
    city = models.CharField(_('Cidade'), max_length=140)
    district = models.CharField(_('Bairro'), max_length=140)
    property_type = models.ForeignKey(PropertyType)
    category = ChainedForeignKey(
        Category,
        chained_field='property_type',
        chained_model_field='property_type'
    )
    rooms = models.PositiveSmallIntegerField(_('Quartos'))
    util_area = models.PositiveSmallIntegerField(
        _('Área útil'),
        blank=True,
        null=True
    )
    total_area = models.PositiveSmallIntegerField(_('Área total'))
    title = models.CharField(_('Titulo'), max_length=140)
    image = models.ImageField(_('Imagem'), upload_to='img/')
    description = models.TextField(_('Descrição'))
    rent_price = models.DecimalField(
        _('Valor do aluguel'),
        max_digits=19,
        decimal_places=10
    )
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        """Set configurations for the Property model."""

        verbose_name = _("Imóvel")
        verbose_name_plural = _('Imóveis')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """Return the absolute url for the model instance."""
        return reverse('properties:show_property', args=[self.id])
