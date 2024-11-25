from django.shortcuts import get_object_or_404, render, redirect
from .models import Airport, City, Continent, Country, Visit
from .forms import AddVisitForm

# Create your views here.
def home(request):
    return render(request, "core/home.html")


def add_visit_country(request, country_slug):
    country = get_object_or_404(Country, slug=country_slug)
    continent = country.continent
    profile = request.user.profile

    if request.method == "POST":
        form = AddVisitForm(request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.profile = request.user
            visit.save()
            return redirect("explore:explore")
    else:
        form = AddVisitForm(initial_country=country, initial_continent=continent)
        return render(request, "visit/add.html", {"form": form, "country": country})
    
def add_visit_city(request, city_slug):
    city = get_object_or_404(City, slug=city_slug)
    country = city.country
    continent = country.continent
    profile = request.user.profile

    print(profile.add_item(city, "city"))

    if request.method == "POST":
        form = AddVisitForm(request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.profile = request.user
            visit.save()
            return redirect("explore:explore")
    else:
        form = AddVisitForm(initial_country=country, initial_continent=continent, initial_city=city)
        return render(request, "visit/add.html", {"form": form, "country": country})
    
def add_visit_airport(request, airport_slug):
    airport = get_object_or_404(Airport, slug=airport_slug)
    city = airport.city
    country = city.country
    continent = country.continent
    profile = request.user.profile

    if request.method == "POST":
        form = AddVisitForm(request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.profile = request.user
            visit.save()
            return redirect("explore:explore")
    else:
        form = AddVisitForm(initial_country=country, initial_continent=continent, initial_city=city, initial_airport=airport)
        return render(request, "visit/add.html", {"form": form, "country": country})
    

def view_visit(request, country_slug):
    country = get_object_or_404(Country, slug=country_slug)
    visits = Visit.objects.filter(country=country)
    for visit in visits:
        print(visit.country)
    return render(request, "visit/view.html", {"visits": visits, "country": country})