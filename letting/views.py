"""Views for the letting application."""

from django.shortcuts import render, get_object_or_404
from .models import Letting


def index(request):
    """Render the list of all lettings."""
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'letting/index.html', context)


def letting(request, letting_id):
    """Render the detail page for a single letting, or 404 if not found."""
    letting = get_object_or_404(Letting, id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting/letting.html', context)


