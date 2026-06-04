"""Views for the main oc_lettings_site application, including error handlers."""

from django.shortcuts import render


def index(request):
    """Render the site home page."""
    return render(request, 'index.html')


def page_not_found(request, exception):
    """Render the custom 404 error page."""
    return render(request, '404.html', status=404)


def server_error(request):
    """Render the custom 500 error page."""
    return render(request, '500.html', status=500)

