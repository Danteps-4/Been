from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug": ("name", )}

@admin.register(models.Currency)
class CurrencyAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}

@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["name", "continent", "population"]
    prepopulated_fields = {"slug": ("name", )}

@admin.register(models.City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    prepopulated_fields = {"slug": ("name", )}

@admin.register(models.Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ["name", "city"]
    prepopulated_fields = {"slug": ("name", )}

@admin.register(models.Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ["profile", "country", "continent", "city", "airport"]