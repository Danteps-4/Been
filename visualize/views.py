from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.models import Country

# Create your views here.
@login_required
def visualize(request):
    countries = list(request.user.profile.countries.all().values("name", "longitude", "latitude"))
    print(countries)
    return render(request, "visualize/visualize.html", {"countries": countries})