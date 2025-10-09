from django.test import TestCase
from hexlet_django_blog.factories import CategoryFactory, ProductFactory


class CategoriesTest(TestCase):
    def setUp(self):
        self.category1 = CategoryFactory(name="foobar")
        self.category2 = CategoryFactory(name="foobar2")
        self.product1 = ProductFactory(category=self.category1)
        self.product2 = ProductFactory(category=self.category2)

    def test_product_list(self):
        response = self.client.get("/products/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.category1.name)
        self.assertContains(response, self.product1.name)
        self.assertContains(response, self.category2.name)
        self.assertContains(response, self.product2.name)

    def test_product_filter_by_category(self):
        response = self.client.get(f"/products/category/{self.category1.id}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product1.name)
        self.assertNotContains(response, self.product2.name)

