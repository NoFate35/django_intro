from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from hexlet_django_blog.factories import ArticleFactory, CommentFactory


class CommentsTest(TestCase):
    def setUp(self):
        self.article = ArticleFactory()
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.comment = CommentFactory(article=self.article, author=self.user.username)

    def test_comment_not_authenticated_user(self):
        comment_data = {"text": "Test comment"}
        response = self.client.post(
            f"/comments/{self.article.id}/add/",
            data=comment_data,
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith("/login/"))

    def test_comment_create_authenticated_user(self):
        self.client.login(username="testuser", password="12345")
        comment_data = {"author": "testuser", "text": "Test comment"}

        response = self.client.post(
            f"/comments/{self.article.id}/add/",
            data=comment_data,
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.article.comments.filter(text="Test comment").exists())

    def test_comment_edit_by_author(self):
        self.client.login(username="testuser", password="12345")

        edit_data = {"author": "test_user", "text": "Edited comment"}
        response = self.client.post(
            f"/comments/{self.comment.id}/edit/", data=edit_data
        )

        self.assertEqual(response.status_code, 302)
        self.comment.refresh_from_db()
        self.assertEqual(self.comment.text, "Edited comment")

    def test_comment_edit_by_other_user(self):
        User.objects.create_user(username="otheruser", password="12345")
        self.client.login(username="otheruser", password="12345")

        edit_data = {"author": "otheruser", "text": "Edited by other user"}
        response = self.client.post(
            reverse("comment_edit", kwargs={"pk": self.comment.id}), data=edit_data
        )

        self.assertEqual(response.status_code, 403)

        self.comment.refresh_from_db()
        self.assertNotEqual(self.comment.text, "Edited by other user")

