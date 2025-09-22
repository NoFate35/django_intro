from django.test import TestCase
from hexlet_django_blog.articles.tests.factories import ArticleFactory


class ArticleTest(TestCase):
    def setUp(self):
        self.article1 = ArticleFactory()
        self.article2 = ArticleFactory()

    def test_create_article(self):
        response = self.client.get("/articles/create/")
        self.assertTemplateUsed(response, "articles/form.html")

        data = {"title": "Test title", "content": "Test content"}
        response = self.client.post("/articles/create/", data=data)
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/articles/")
        self.assertContains(response, data["title"])

    def test_update_article(self):
        response = self.client.get(f"/articles/{self.article1.id}/update/")
        self.assertTemplateUsed(response, "articles/form.html")
        self.assertContains(response, self.article1.title)
        self.assertContains(response, self.article1.content)

        data = {"title": "Updated title", "content": "Updated content"}
        response = self.client.post(f"/articles/{self.article1.id}/update/", data=data)
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/articles/")
        self.assertContains(response, data["title"])

    def test_delete_article(self):
        response = self.client.get("/articles/")
        self.assertContains(response, self.article2.title)

        response = self.client.get(f"/articles/{self.article2.id}/delete/")
        self.assertTemplateUsed(response, "articles/article_confirm_delete.html")

        response = self.client.post(f"/articles/{self.article2.id}/delete/")
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/articles/")
        self.assertNotContains(response, self.article2.title)

