from django.forms import ModelForm
from django import forms
from hexlet_django_blog.article.models import ArticleComment

from .models import Article

class ArticleCommentForm(ModelForm):
    class Meta:
        model = ArticleComment
        fields = ["content"]


class ArticleForm(ModelForm):
    name = forms.CharField(max_length=100, required=True)
    body = forms.CharField(max_length=200, required=True)
    class Meta:
        model = Article
        fields = ["name", "body"]