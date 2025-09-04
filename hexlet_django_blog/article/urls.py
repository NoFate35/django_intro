from django.urls import path
from hexlet_django_blog.article import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='articles_index'),
    path("comment/", views.CommentArticleView.as_view(), name='comment_create'),
    path("<str:name>/", views.ArticleView.as_view()),
    ]