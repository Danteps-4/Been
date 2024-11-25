from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from core.models import Country, Continent, City, Airport
from account.models import Profile
from core.forms import SearchForm

# Create your views here.
@login_required
def select(request):
    profile = get_object_or_404(Profile, user=request.user)
    num_countries = profile.countries.all().count()
    num_continents = profile.continents.all().count()
    num_cities = profile.cities.all().count()
    num_airports = profile.airports.all().count()
    return render(request, "select/select.html", {"num_countries": num_countries, "num_continents": num_continents, "num_cities": num_cities, "num_airports": num_airports})

@login_required
def my_selection_item(request, selection_item):
    profile = get_object_or_404(Profile, user=request.user)
    search_form = SearchForm(request.GET or None)
    q = request.GET.get("q", "")

    if selection_item == "countries":
        countries = profile.countries.filter(name__icontains=q) if q else profile.countries.all()
        num_countries = countries.count()
        return render(request, "select/my_selection_item.html", {"countries": countries, "num_countries": num_countries, "selection_item": "countries", "search_form": search_form})
    elif selection_item == "continents":
        continents = profile.continents.filter(name__icontains=q) if q else profile.continents.all()
        num_continents = continents.count()
        return render(request, "select/my_selection_item.html", {"continents": continents, "num_continents": num_continents, "selection_item": "continents", "search_form": search_form})
    elif selection_item == "cities":
        cities = profile.cities.filter(name__icontains=q) if q else profile.cities.all()
        num_cities = cities.count()
        return render(request, "select/my_selection_item.html", {"cities": cities, "num_cities": num_cities, "selection_item": "cities", "search_form": search_form})
    elif selection_item == "airports":
        airports = profile.airports.filter(name__icontains=q) if q else profile.airports.all()
        num_airports = airports.count()
        return render(request, "select/my_selection_item.html", {"airports": airports, "num_airports": num_airports, "selection_item": "airports", "search_form": search_form})