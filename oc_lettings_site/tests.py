"""Tests for the oc_lettings_site custom HTTP error handlers (404 and 500)."""

from django.test import SimpleTestCase, override_settings
from django.urls import path, include
from django.http import Http404, HttpResponse


def view_404(request):
    """Stub view that raises Http404 to trigger the 404 handler."""
    raise Http404


def view_500(request):
    """Stub view that raises an exception to trigger the 500 handler."""
    raise Exception("Erreur volontaire")


def home(request):
    """Stub home view returning a plain HTTP 200 response."""
    return HttpResponse("home")


profile_urls = ([path("", home, name="index")], "profile")
letting_urls = ([path("", home, name="index")], "letting")

urlpatterns = [
    path("", home, name="index"),
    path("profiles/", include(profile_urls)),
    path("lettings/", include(letting_urls)),
    path("test-404/", view_404),
    path("test-500/", view_500),
]

handler404 = "oc_lettings_site.views.page_not_found"
handler500 = "oc_lettings_site.views.server_error"


@override_settings(ROOT_URLCONF=__name__)
class TestErrorHandlers(SimpleTestCase):
    """Tests that the custom 404 and 500 handlers return correct responses."""

    def test_404_retourne_bon_status(self):
        """A request to an unknown URL should return HTTP 404."""
        response = self.client.get("/url-dont-exist/")
        self.assertEqual(response.status_code, 404)

    def test_500_retourne_bon_status(self):
        """An unhandled server exception should return HTTP 500."""
        self.client.raise_request_exception = False
        response = self.client.get("/test-500/")
        self.assertEqual(response.status_code, 500)

    def test_404_contient_lien_profiles(self):
        """The 404 page should contain a link to the Profiles section."""
        response = self.client.get("/url-dont-exist/")
        self.assertContains(response, "Profiles", status_code=404)

    def test_404_contient_lien_lettings(self):
        """The 404 page should contain a link to the Lettings section."""
        response = self.client.get("/url-dont-exist/")
        self.assertContains(response, "Lettings", status_code=404)
