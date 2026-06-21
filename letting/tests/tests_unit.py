"""Unit tests for the letting application: models and URL resolution."""

from django.test import TestCase
from letting.models import Address, Letting
from django.urls import reverse, resolve
from letting import views


class AddressModelTest(TestCase):
    """Tests for the Address model."""

    def setUp(self):
        """Create a sample Address instance."""
        self.address = Address.objects.create(
            number=123,
            street="Main Street",
            city="Springfield",
            state="IL",
            zip_code=62701,
            country_iso_code="USA",
        )

    def test_str_returns_number_and_street(self):
        """__str__ should return '{number} {street}'."""
        self.assertEqual(str(self.address), "123 Main Street")


class LettingModelTest(TestCase):
    """Tests for the Letting model."""

    def setUp(self):
        """Create a sample Letting instance with an address."""
        address = Address.objects.create(
            number=1,
            street="Rue de la Paix",
            city="Paris",
            state="FR",
            zip_code=75001,
            country_iso_code="FRA",
        )
        self.letting = Letting.objects.create(title="Nice apartment", address=address)

    def test_str_returns_title(self):
        """__str__ should return the letting title."""
        self.assertEqual(str(self.letting), "Nice apartment")


class LettingUrlsTest(TestCase):
    """Tests for the letting URL configuration."""

    def test_index_url_resolves(self):
        """The index URL should resolve to /lettings/ and map to views.index."""
        url = reverse("letting:index")
        self.assertEqual(url, "/lettings/")
        self.assertEqual(resolve(url).func, views.index)

    def test_letting_detail_url_resolves(self):
        """The detail URL should resolve to /lettings/<id>/ and map to views.letting."""
        url = reverse("letting:letting", args=[1])
        self.assertEqual(url, "/lettings/1/")
        self.assertEqual(resolve(url).func, views.letting)
