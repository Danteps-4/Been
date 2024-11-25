from django.urls import path
from . import views

app_name = "visuelize"

urlpatterns = [
    path("", views.visualize, name="visualize"),
]
