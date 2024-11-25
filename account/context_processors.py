from .models import Profile

def avatar(request):
    context = {}
    if request.user.is_authenticated:
        avatar = Profile.objects.get(user=request.user)
        context["avatar"] = avatar
    return context

def total_countries_visited(request):
    context = {}
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        context["total_countries_visited"] = profile.total_countries_visited()
    return context