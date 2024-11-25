from django.urls import path
from . import views

app_name = "select"

urlpatterns = [
    path("", views.select, name="select"),
    path("<str:selection_item>/", views.my_selection_item, name="my_selection_item"),
]