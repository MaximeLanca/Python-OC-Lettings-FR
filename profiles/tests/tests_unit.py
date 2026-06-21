"""Unit tests for the profiles application: models and URL resolution."""

from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile
from django.urls import reverse, resolve
from profiles import views


class ProfileModelTest(TestCase):
    """Tests for the Profile model."""

    def setUp(self):
        """Create a sample User and associated Profile."""
        self.user = User.objects.create_user(username="alice", password="pass")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")

    def test_str_returns_username(self):
        """__str__ should return the associated username."""
        self.assertEqual(str(self.profile), "alice")


class ProfileUrlsTest(TestCase):
    """Tests for the profiles URL configuration."""

    def test_index_url_resolves(self):
        """The index URL should resolve to /profiles/ and map to views.index."""
        url = reverse("profile:index")
        self.assertEqual(url, "/profiles/")
        self.assertEqual(resolve(url).func, views.index)

    def test_profile_detail_url_resolves(self):
        """The detail URL should resolve to /profiles/<username>/ and map to views.profile."""
        url = reverse("profile:profile", args=["alice"])
        self.assertEqual(url, "/profiles/alice/")
        self.assertEqual(resolve(url).func, views.profile)
