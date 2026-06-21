"""Integration tests for the letting application views."""

from django.test import TestCase, Client
from django.urls import reverse
from letting.models import Address, Letting


class LettingViewsTest(TestCase):
    """End-to-end tests for the letting index and detail views."""

    def setUp(self):
        """Create a letting with an address for use across all tests."""
        self.client = Client()
        address = Address.objects.create(
            number=10,
            street="Baker Street",
            city="London",
            state="UK",
            zip_code=10001,
            country_iso_code="GBR",
        )
        self.letting = Letting.objects.create(title="Studio London", address=address)

    def test_index_view_status_200(self):
        """Index view should return HTTP 200."""
        response = self.client.get(reverse("letting:index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        """Index view should render the letting/index.html template."""
        response = self.client.get(reverse("letting:index"))
        self.assertTemplateUsed(response, "letting/index.html")

    def test_index_view_contains_letting_title(self):
        """Index view should display the letting title in the response."""
        response = self.client.get(reverse("letting:index"))
        self.assertContains(response, "Studio London")

    def test_letting_detail_view_status_200(self):
        """Detail view should return HTTP 200 for an existing letting."""
        url = reverse("letting:letting", args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_letting_detail_view_context(self):
        """Detail view context should expose the correct letting title."""
        url = reverse("letting:letting", args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.context["title"], "Studio London")

    def test_letting_detail_404_on_missing_id(self):
        """Detail view should return HTTP 404 for a non-existent letting id."""
        url = reverse("letting:letting", args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
