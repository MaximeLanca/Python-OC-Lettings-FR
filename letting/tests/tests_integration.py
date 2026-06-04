from django.test import TestCase, Client
from django.urls import reverse
from letting.models import Address, Letting


class LettingViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        address = Address.objects.create(
            number=10,
            street="Baker Street",
            city="London",
            state="UK",
            zip_code=10001,
            country_iso_code="GBR"
        )
        self.letting = Letting.objects.create(title="Studio London",address=address)

    def test_index_view_status_200(self):
        response = self.client.get(reverse('letting:index'))
        self.assertEqual(response.status_code, 200)

    def test_index_view_uses_correct_template(self):
        response = self.client.get(reverse('letting:index'))
        self.assertTemplateUsed(response, 'letting/index.html')

    def test_index_view_contains_letting_title(self):
        response = self.client.get(reverse('letting:index'))
        self.assertContains(response, "Studio London")

    def test_letting_detail_view_status_200(self):
        url = reverse('letting:letting', args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_letting_detail_view_context(self):
        url = reverse('letting:letting', args=[self.letting.id])
        response = self.client.get(url)
        self.assertEqual(response.context['title'], "Studio London")

    def test_letting_detail_404_on_missing_id(self):
        url = reverse('letting:letting', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    
