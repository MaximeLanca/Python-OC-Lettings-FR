from django.test import TestCase
from letting.models import Address, Letting
from django.urls import reverse, resolve
from letting import views


"""Models Test"""

class AddressModelTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=123,
            street="Main Street",
            city="Springfield",
            state="IL",
            zip_code=62701,
            country_iso_code="USA"
        )
    def test_str_returns_number_and_street(self):
        self.assertEqual(str(self.address), "123 Main Street")

class LettingModelTest(TestCase):
    def setUp(self):
        address = Address.objects.create(
            number=1,
            street="Rue de la Paix",
            city="Paris",
            state="FR",
            zip_code=75001,
            country_iso_code="FRA"
        )
        self.letting = Letting.objects.create(title="Nice apartment", address=address)

    def test_str_returns_title(self):
        self.assertEqual(str(self.letting), "Nice apartment")

"""URL Test"""

class LettingUrlsTest(TestCase):
    def test_index_url_resolves(self):
        url = reverse('letting:index')
        self.assertEqual(url, '/lettings/')
        self.assertEqual(resolve(url).func, views.index)

    def test_letting_detail_url_resolves(self):
        url=reverse('letting:letting', args=[1])
        self.assertEqual(url, '/lettings/1/')
        self.assertEqual(resolve(url).func, views.letting)