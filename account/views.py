from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, EditProfileForm, UserProfileForm
from django.contrib.auth import login, logout, authenticate
from .models import Profile
from core.models import Visit

# Create your views here.

# -----LOGIN SIGN UP LOGOUT-----
def sign_up(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("film:home")
    else:
        form = RegistrationForm()
    return render(request, "registration/sign_up.html", {"form": form})

@login_required
def log_out(request):
    logout(request)
    return redirect("login")


# -----PROFILE-----
@login_required
def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    num_countries = profile.total_countries_visited()
    world_percentage = profile.world_percentage()
    return render(request, "profile/view.html", {"num_countries": num_countries, "world_percentage": world_percentage, "num_continents": profile.continents.count(), "num_cities": profile.cities.count(), "num_airports": profile.airports.count()})

@login_required
def profile_edit(request):
    if request.method == "POST":
        user_form = EditProfileForm(instance=request.user, data=request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("account:profile_view")
    else:
        user_form = EditProfileForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)
    return render(request, "profile/edit.html", {"user_form": user_form, "profile_form": profile_form})

@login_required
def profile_view_visits(request):
    visits = Visit.objects.filter(profile=request.user)
    countries = []
    cities = []
    airports = []
    for visit in visits:
        if visit.country not in countries:
            countries.append(visit.country)
        if visit.city is not None and visit.city not in cities:
            cities.append(visit.city)
        if visit.airport is not None and visit.airport not in airports:
            airports.append(visit.airport)
    return render(request, "profile/view_visits.html", {"countries": countries, "cities": cities, "airports": airports})

@login_required
def add_friend(request, profile_slug):
    profile_to_add = get_object_or_404(Profile, slug=profile_slug)
    profile = get_object_or_404(Profile, user=request.user)

    if profile.is_friend(profile_to_add.user):
        return redirect("compare:profile_view")
    else:
        try:
            profile.friends.add(profile_to_add.user)
        except Exception as e:
            print(e)
        return redirect("account:profile_view")
    
@login_required
def view_friends(request):
    friends = get_object_or_404(Profile, user=request.user).friends.all()
    return render(request, "profile/friends.html", {"friends": friends})

@login_required
def delete_friend(request, friend):
    friend = get_object_or_404(Profile, slug=friend)
    profile = get_object_or_404(Profile, user=request.user)
    
    profile.friends.remove(friend.user)
    return redirect("account:profile_view")