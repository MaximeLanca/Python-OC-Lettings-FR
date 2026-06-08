"""Views for the profiles application."""

import logging

from django.shortcuts import render, get_object_or_404
from .models import Profile

logger = logging.getLogger('profiles')


def index(request):
    """Render the list of all user profiles."""
    profiles_list = Profile.objects.all()
    logger.info("Profiles index accessed, %d profiles found", profiles_list.count())
    context = {'profiles_list': profiles_list}
    return render(request, 'profile/index.html', context)


def profile(request, username):
    """Render the detail page for a single profile, or 404 if not found."""
    profile = get_object_or_404(Profile, user__username=username)
    logger.info("Profile detail accessed: username='%s'", username)
    context = {'profile': profile}
    return render(request, 'profile/profile.html', context)
