from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_("Название категории"), max_length=100)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(_("Название"), max_length=255)
    avg_price = models.DecimalField(_("Средняя цена"), max_digits=10, decimal_places=2, default=0)
    avg_rating = models.FloatField(_("Средний рейтинг"), default=0)
    coordinates_x = models.FloatField(_("Координаты X"), default=0)
    coordinates_y = models.FloatField(_("Координаты Y"), default=0)
    description = models.TextField(_("Описание"), blank=True)
    phone = models.CharField(_("Телефон"), max_length=20, blank=True)
    whatsapp = models.CharField(_("WhatsApp"), max_length=50, blank=True)
    instagram = models.URLField(_("Instagram"), blank=True)
    address = models.TextField(_("Адрес"), blank=True)
    categories = models.ManyToManyField(Category, related_name="places")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="places")

    def __str__(self):
        return self.name
