from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from hexlet_django_blog.articles.models import Article
from hexlet_django_blog.comments.models import Comment

from .forms import CommentForm


# BEGIN (write your solution here)
class CommentAddView(View):
    @login_required
    def get(self, request, *args, **kwargs):
        form = CommentForm()
        return render(request, "comments/comment_form.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        article_id = kwargs.get("article_id")
        if form.is_valid():
        	comment_article = Article.objects.get(id=article_id)
        	comment_author = form.cleaned_data['author']
        	comment_text = form.cleaned_data['text']
        	Comment.objects.create(article=comment_article, author=comment_author, text=comment_text)
        	return render(request, "articles/detail.html", {"article": comment_article})
        return render(request, "comments/comment_form.html", {"form": form})

class CommentEditView(View):
    @login_required
    def get(self, request, *args, **kwargs):
        comment_id = kwargs.get("pk")
        comment = Comment.objects.get(id=comment_id)
        form = CommentForm(instance=comment)
        return render(request, "comments/comment_form.html", {"form": form})
    def post(self, request, *args, **kwargs):
        comment_id = kwargs.get("pk")
        comment = Comment.objects.get(id=comment_id)
        comment_article = comment.article
        form = CommentForm(request.POST)
        if form.is_valid():
            comment.text = form.cleaned_data['text']
            comment.save()
            return render(request, "articles/detail.html", {"article": comment_article})
        form = CommentForm(instance=comment)
        return render(request, "comments/comment_form.html", {"form": form})
# END