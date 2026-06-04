from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile
from django.urls import reverse, resolve
from profiles import views


"""Models Test"""

class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="alice",
            password="pass"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city="Paris"
        )

    def test_str_returns_username(self):
        self.assertEqual(str(self.profile), "alice")


"""URL Test"""

class ProfileUrlsTest(TestCase):
    def test_index_url_resolves(self):
        url = reverse('profile:index')
        self.assertEqual(url, '/profiles/')
        self.assertEqual(resolve(url).func, views.index)

    def test_profile_detail_url_resolves(self):
        url = reverse('profile:profile', args=["alice"])
        self.assertEqual(url, '/profiles/alice/')
        self.assertEqual(resolve(url).func, views.profile)
