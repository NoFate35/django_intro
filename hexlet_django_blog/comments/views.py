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
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = CommentForm()
        return render(request, "comments/comment_form.html", {"form": form})

    @method_decorator(login_required(login_url="/login/"))
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        article_id = kwargs.get("article_id")
        if form.is_valid():
            comment_article = Article.objects.get(id=article_id)
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            Comment.objects.create(article=comment_article, author=comment_author, text=comment_text)
            return redirect ('article_detail', comment_article.id)
        return render(request, "comments/comment_form.html", {"form": form})

class CommentEditView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        comment_id = kwargs.get("pk")
        comment = Comment.objects.get(id=comment_id)
        if comment.author == request.user.username:
            form = CommentForm(instance=comment)
            return render(request, "comments/comment_form.html", {"form": form})
        return HttpResponse(status=403)

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        comment_id = kwargs.get("pk")
        comment = Comment.objects.get(id=comment_id)
        form = CommentForm(request.POST)
        if comment.author == request.user.username:
            if form.is_valid():
                comment.text = form.cleaned_data['text']
                comment.save()
                return redirect ('article_detail', comment.article.id)
        return HttpResponse(status=403)
# END