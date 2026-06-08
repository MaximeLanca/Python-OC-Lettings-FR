"""Views for the letting application."""

import logging

from django.shortcuts import render, get_object_or_404
from .models import Letting

logger = logging.getLogger('letting')


def index(request):
    """Render the list of all lettings."""
    lettings_list = Letting.objects.all()
    logger.info("Letting index accessed, %d lettings found", lettings_list.count())
    context = {'lettings_list': lettings_list}
    return render(request, 'letting/index.html', context)


def letting(request, letting_id):
    """Render the detail page for a single letting, or 404 if not found."""
    letting = get_object_or_404(Letting, id=letting_id)
    logger.info("Letting detail accessed: id=%s title='%s'", letting_id, letting.title)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting/letting.html', context)


