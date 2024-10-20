from django.db import models
from apps.main.models import BaseModel

from ckeditor.fields import RichTextField


class Country(BaseModel):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/countries/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Davlatlar'
        verbose_name = 'Davlat'


class Destination(BaseModel):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/destinations/')
    country = models.ForeignKey(
        Country, models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def lowest_price(self):
        try:
            tours = self.tours.order_by('price')
            return tours.first().price
        except:
            return 0


class Tour(BaseModel):
    name = models.CharField(max_length=250)
    description = RichTextField(blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    image = models.ImageField(upload_to='images/tours/')
    destinations = models.ManyToManyField(Destination, blank=True, related_name='tours')
    countries = models.ManyToManyField(Country, blank=True)

    def __str__(self):
        return self.name