"""Integration tests for the profiles application views."""

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileViewsTest(TestCase):
    """End-to-end tests for the profiles index and detail views."""

    def setUp(self):
        """Create a user and associated profile for use across all tests."""
        self.client = Client()
        self.user = User.objects.create_user(username="bob", password="pass")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Lyon")

    def test_index_view_status_200(self):
        """Index view should return HTTP 200."""
        response = self.client.get(reverse("profile:index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        """Index view should render the profile/index.html template."""
        response = self.client.get(reverse("profile:index"))
        self.assertTemplateUsed(response, "profile/index.html")

    def test_index_view_contains_username(self):
        """Index view should display the username in the response."""
        response = self.client.get(reverse("profile:index"))
        self.assertContains(response, "bob")

    def test_profile_detail_view_status_200(self):
        """Detail view should return HTTP 200 for an existing profile."""
        url = reverse("profile:profile", args=[self.user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_profile_detail_view_context(self):
        """Detail view context should expose the correct favorite city."""
        url = reverse("profile:profile", args=[self.user.username])
        response = self.client.get(url)
        self.assertEqual(response.context["profile"].favorite_city, "Lyon")

    def test_profile_detail_404_on_missing_username(self):
        """Detail view should return HTTP 404 for a non-existent username."""
        url = reverse("profile:profile", args=["unknown_user"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
