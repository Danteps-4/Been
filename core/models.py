from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
def user_directory_path(instance, filename):
    return f"flags/{instance.id}/{filename}"

def user_directory_path_landscape(instance, filename):
    return f"landscapes/{instance.id}/{filename}"

User = get_user_model()

class Continent(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name
    
class Currency(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    continent = models.ForeignKey(Continent, on_delete=models.PROTECT, related_name="countries")
    population = models.IntegerField()
    currency = models.ForeignKey(Currency, on_delete=models.SET_DEFAULT, default=1)
    territory = models.IntegerField()
    domain = models.CharField(max_length=3)
    flag = models.ImageField(upload_to=user_directory_path, default="flags/default.jpg")
    landscape = models.ImageField(upload_to=user_directory_path_landscape, default="landscapes/default.jpg")
    latitude = models.FloatField(default=1)
    longitude = models.FloatField(default=1)

    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}, {self.country}"
    
class Airport(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name}, {self.city}"
    
class Visit(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, blank=True)
    airport = models.ForeignKey(Airport, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Visit to {self.country.name} by {self.profile.username}"

@receiver(post_save, sender=Visit)
def add_country_to_profile(sender, instance, created, **kwargs):
    if created and instance.country:
        profile = instance.profile.profile
        if instance.country not in profile.countries.all():
            profile.countries.add(instance.country)
