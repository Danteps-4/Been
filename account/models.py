from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from core.models import Country, Continent, City, Airport, Visit

# Create your models here.
def user_directory_path(instance, filename):
    return f"users/avatars/{instance.user.id}/{filename}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to=user_directory_path, default="users/avatar.jpg")
    bio = models.TextField(max_length=500, blank=True)
    countries = models.ManyToManyField(Country, blank=True)
    continents = models.ManyToManyField(Continent, blank=True)
    cities = models.ManyToManyField(City, blank=True)
    airports = models.ManyToManyField(Airport, blank=True)
    friends = models.ManyToManyField(User, blank=True, related_name="friends")

    def total_countries_visited(self):
        return self.countries.count()
    
    def total_continents(self):
        return self.continents.count()
    
    def total_cities(self):
        return self.cities.count()
    
    def total_airports(self):
        return self.airports.count()
    
    def world_percentage(self):
        return round((self.total_countries_visited()*100) / 195)
    
    def add_item(self, item, string):
        try:
            if string == "continent":
                if item not in self.continents:
                    self.continents.add(item)
            elif string == "country":
                if item not in self.countries:
                    self.countries.add(item)
            elif string == "city":
                if item not in self.cities:
                    self.cities.add(item)
            elif string == "airport":
                if item not in self.airports:
                    self.airports.add(item)
        except Exception as e:
            return f"Error: {e}"
        return f"Added {item}"
    
    def is_friend(self, friend):
        if friend in self.friends.all():
            return True
        return False

    def __str__(self):
        return f"Profile {self.user.username}"
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
