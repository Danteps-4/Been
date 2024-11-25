from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path('add-visit/country/<str:country_slug>/', views.add_visit_country, name='add_visit_country'),
    path('add-visit/city/<str:city_slug>/', views.add_visit_city, name='add_visit_city'),
    path('add-visit/airport/<str:airport_slug>/', views.add_visit_airport, name='add_visit_airport'),
    path("view-visit/<slug:country_slug>/", views.view_visit, name="view_visit"),
]