from django.test import SimpleTestCase, override_settings
from django.urls import path, include
from django.http import Http404, HttpResponse


def view_404(request):
    raise Http404

def view_500(request):
    raise Exception("Erreur volontaire")

def home(request):
    return HttpResponse("home")

profile_urls = ([path('', home, name='index')], 'profile')
letting_urls = ([path('', home, name='index')], 'letting')

urlpatterns = [
    path('', home, name='index'),
    path('profiles/', include(profile_urls)),
    path('lettings/', include(letting_urls)),
    path('test-404/', view_404),
    path('test-500/', view_500),
]

handler404 = 'oc_lettings_site.views.page_not_found'
handler500 = 'oc_lettings_site.views.server_error'


@override_settings(ROOT_URLCONF=__name__)
class TestErrorHandlers(SimpleTestCase):

    def test_404_retourne_bon_status(self):
        response = self.client.get('/url-dont-exist/')
        self.assertEqual(response.status_code, 404)

    def test_500_retourne_bon_status(self):
        self.client.raise_request_exception = False 
        response = self.client.get('/test-500/')
        self.assertEqual(response.status_code, 500)

    def test_404_contient_lien_profiles(self):
        response = self.client.get('/url-dont-exist/')
        self.assertContains(response, 'Profiles', status_code=404)

    def test_404_contient_lien_lettings(self):
        response = self.client.get('/url-dont-exist/')
        self.assertContains(response, 'Lettings', status_code=404)