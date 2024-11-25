from django.urls import path
from . import views

app_name = "compare"

urlpatterns = [
    path("", views.view_all, name="view_all"),
    path("load-more-profiles", views.load_more_profiles, name="load_more_profiles"),
    path("<slug:profile_slug>/", views.compare, name="compare"),
]
