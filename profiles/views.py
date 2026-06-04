"""Views for the profiles application."""

from django.shortcuts import render, get_object_or_404
from .models import Profile


def index(request):
    """Render the list of all user profiles."""
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profile/index.html', context)


def profile(request, username):
    """Render the detail page for a single profile, or 404 if not found."""
    profile = get_object_or_404(Profile, user__username=username)
    context = {'profile': profile}
    return render(request, 'profile/profile.html', context)
