from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class ArticlesTest(TestCase):
    def test_articles_list(self):
        response = self.client.get(reverse("homepage"))
        self.assertEqual(response.status_code, 302)
