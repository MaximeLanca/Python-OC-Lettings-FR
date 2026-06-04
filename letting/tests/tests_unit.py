from django.test import TestCase
from letting.models import Address, Letting
from django.urls import reverse, resolve
from letting import views


"""Models Test"""

class AddressModelTest(TestCase):
    def setUp(self):
        self.address = Address.object.create(
            number=123,
            street="Main Street",
            city="Springfield"
            state="IL"
            zip_code=62701,
            country_iso_code="USA"
        )
    def test_str_returns_number_and_street(self):
        self.assertEqual(str(self.address), "123 Main Street")

class LettingModelTest(TestCase):
    def setUp(self):
        address = Address.object.create(
            number=1,
            street="Rue de la Paix",
            city="Paris",
            state="FR",
            zip_code=75001,
            country_iso_code="FRA"
        )
        self.letting = Letting.object.create(title="NIce apartment", address=address)

    def test_str_returns_title(self):
        self.assertEqual(str(self.letting), "Nice apartement")

    def test_address_relationship(self):
        self.assertEqual(self.letting.Address.city, "Paris")

"""URL Test"""

class LettingUrlsTest(TestCase):
    def test_index_url_resolves(self):
        url = reverse('letting:index')
        self.asserEqual(url, '/lettings')
        self.assertEqual(resolve(url).func, views.index)

    def test_letting_detail_url_resolves(self):
        url=reverse('letting:letting', args=[1])
        self.assertEqual(url, '/lettings/1/')
        self.assertEqual(resolve(url.func, views.letting))