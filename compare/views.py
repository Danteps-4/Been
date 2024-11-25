from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.http import JsonResponse
from core.forms import SearchForm
from account.models import Profile

# Create your views here.

@login_required
def view_all(request):
    profiles = Profile.objects.exclude(user=request.user)[:1]

    search_form = SearchForm(request.GET or None)
    q = request.GET.get("q", "")
    results = []

    if q:
        results = Profile.objects.filter(slug__icontains=q).exclude(user=request.user)
        return render(request, "compare/all.html", {"search_form": search_form, "profiles": results})

    return render(request, "compare/all.html", {"search_form": search_form, "profiles": profiles})

@login_required
def load_more_profiles(request):
    offset = int(request.GET.get("offset", 0))
    limit = 1

    profiles = Profile.objects.exclude(user=request.user)[offset:offset+limit]
    profiles_data = [
        {
            "username": profile.user.username,
            "avatar_url": profile.avatar.url,
            "slug": profile.slug
        }
        for profile in profiles
    ]
    return JsonResponse({"profiles": profiles_data})

@login_required
def compare(request, profile_slug):
    profile_other = get_object_or_404(Profile, slug=profile_slug)
    profile_me = get_object_or_404(Profile, user=request.user)

    are_friends = profile_me.is_friend(profile_other.user)

    return render(request, "compare/comparing.html", {"profile_me": profile_me, "profile_other": profile_other, "are_friends": are_friends})