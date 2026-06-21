"""Views for the main oc_lettings_site application, including error handlers."""

import logging

from django.shortcuts import render

logger = logging.getLogger("oc_lettings_site")


def index(request):
    """Render the site home page."""
    logger.info("Home page accessed")
    return render(request, "index.html")


def page_not_found(request, exception):
    """Render the custom 404 error page."""
    logger.warning("404 error: path='%s' exception=%s", request.path, exception)
    return render(request, "404.html", status=404)


def server_error(request):
    """Render the custom 500 error page."""
    logger.error("500 error: path='%s'", request.path)
    return render(request, "500.html", status=500)
