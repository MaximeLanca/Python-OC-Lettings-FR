"""Admin registration for the profiles application models."""

from django.contrib import admin

from .models import Profile

admin.site.register(Profile)
