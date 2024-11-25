from django.shortcuts import get_object_or_404, render
from core.models import Continent, Country, City, Airport
from core.forms import SearchForm

# Create your views here.
def explore(request):
    q = request.GET.get("q", "")
    search_form = SearchForm(request.GET or None)
    results = []

    continents = Continent.objects.prefetch_related("countries").all()
    
    for continent in continents:
        filtered_countries = continent.countries.filter(name__icontains=q) if q else continent.countries.all()

        # Agregar continente a la lista solo si tiene países que coinciden
        if filtered_countries.exists():
            continent.filtered_countries = filtered_countries
            results.append(continent)


    return render(request, "explore/explore.html", {"continents": results, "search_form": search_form})


def country_single(request, country):
    country = get_object_or_404(Country, slug=country)
    point = {"latitude": country.latitude, "longitude": country.longitude}
    return render(request, "country/single.html", {"country": country, "point": point})

def continent_single(request, continent):
    continent = get_object_or_404(Continent, slug=continent)
    return render(request, "continent/continent.html", {"continent": continent})

def city_single(request, city):
    city = get_object_or_404(City, slug=city)
    return render(request, "city/city.html", {"city": city})

def airport_single(request, airport):
    airport = get_object_or_404(Airport, slug=airport)
    return render(request, "airport/airport.html", {"airport": airport})
