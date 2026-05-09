from django.test import TestCase
from django.urls import reverse
from core.models import ShortenedURL


class URLShortenerTests(TestCase):

    def test_shorten_url(self):
        response = self.client.post(
            '/api/urls/',
            {'long_url': 'https://www.google.com'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertIn('short_code', response.json())
        self.assertIn('short_url', response.json())

    def test_list_urls(self):
        ShortenedURL.objects.create(long_url='https://www.google.com')
        response = self.client.get('/api/urls/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_redirect(self):
        obj = ShortenedURL.objects.create(long_url='https://www.google.com')
        response = self.client.get(f'/{obj.short_code}/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], 'https://www.google.com')

    def test_delete_url(self):
        obj = ShortenedURL.objects.create(long_url='https://www.google.com')
        response = self.client.delete(f'/api/urls/{obj.short_code}/')
        self.assertEqual(response.status_code, 204)

    def test_delete_nonexistent(self):
        response = self.client.delete('/api/urls/invalid123/')
        self.assertEqual(response.status_code, 404)

    def test_invalid_url(self):
        response = self.client.post(
            '/api/urls/',
            {'long_url': 'not-a-url'},
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)