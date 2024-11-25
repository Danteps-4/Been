from django.urls import path
from . import views

app_name = "explore"

urlpatterns = [
    path("", views.explore, name="explore"),
    path("countries/<slug:country>/", views.country_single, name="country_single"),
    path("continents/<slug:continent>/", views.continent_single, name="continent_single"),
    path("cities/<slug:city>/", views.city_single, name="city_single"),
    path("airports/<slug:airport>/", views.airport_single, name="airport_single"),
]