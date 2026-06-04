from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="bob",
            password="pass"
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city="Lyon"
        )

    def test_index_view_status_200(self):
        response = self.client.get(reverse('profile:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        response = self.client.get(reverse('profile:index'))
        self.assertTemplateUsed(response, 'profile/index.html')

    def test_index_view_contains_username(self):
        response = self.client.get(reverse('profile:index'))
        self.assertContains(response, "bob")

    def test_profile_detail_view_status_200(self):
        url = reverse('profile:profile', args=[self.user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_profile_detail_view_context(self):
        url = reverse('profile:profile', args=[self.user.username])
        response = self.client.get(url)
        self.assertEqual(response.context['profile'].favorite_city, "Lyon")

    def test_profile_detail_404_on_missing_username(self):
        url = reverse('profile:profile', args=["unknown_user"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
