from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.name


class Apartment(models.Model):

    url_object = models.URLField()
    metro_name = models.CharField(max_length=32, blank=True)
    metro_distance = models.CharField(max_length=50, blank=True)
    metro_distance_number = models.CharField(max_length=32, blank=True)
    total_square = models.CharField(max_length=32, blank=True)
    living_square = models.CharField(max_length=32, blank=True)
    floor_number = models.CharField(max_length=32, blank=True)
    floor_total = models.CharField(max_length=32, blank=True)
    count_room = models.CharField(max_length=32, blank=True)
    material = models.CharField(max_length=32, blank=True)
    balcony_type = models.CharField(max_length=32, blank=True)
    is_home_appliances = models.CharField(max_length=32, blank=True)
    is_furniture = models.CharField(max_length=32, blank=True)
    year_public = models.CharField(max_length=32, blank=True)
    month_public = models.CharField(max_length=32, blank=True)
    day_public = models.CharField(max_length=32, blank=True)
    time_public = models.CharField(max_length=16, blank=True)
    cost = models.CharField(max_length=32, blank=True)
    currency = models.CharField(max_length=32, blank=True)
    street = models.CharField(max_length=32)
    house_number = models.CharField(max_length=32, blank=True)
    city = models.CharField(max_length=32, blank=True)
    area_city = models.CharField(max_length=32, blank=True)
    advertising_object = models.CharField(max_length=70, blank=True)
    category = models.ManyToManyField(Category)