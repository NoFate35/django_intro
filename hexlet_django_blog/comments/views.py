from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from hexlet_django_blog.articles.models import Article
from hexlet_django_blog.comments.models import Comment

from .forms import CommentForm



# BEGIN (write your solution here)
@method_decorator(login_required, name="dispatch")
class CommentAddView(View):
    template_name = "comments/comment_form.html"
    def get(self, request, *args, **kwargs):
        comment_article = get_object_or_404(Article, pk=kwargs.get("article_id"))
        form = CommentForm()
        return  render(request, "articles/detail.html", {"article": comment_article, "form": form})

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        comment_article = get_object_or_404(Article, pk=kwargs.get("article_id"))
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = comment_article
            comment.author = request.user.username
            comment.save()
            return redirect (comment_article.get_absolute_url())
        return  render(request, self.template_name, {"article": comment_article, "form": form})


@method_decorator(login_required, name="dispatch")
class CommentEditView(View):
    
    template_name = "comments/comment_form.html"
    
    def dispatch(self, request, *args, **kwargs):
        self.comment = get_object_or_404(Comment, pk=kwargs["pk"])
        if request.user.username != self.comment.author:
            return HttpResponse(status=403)
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
            form = CommentForm(instance=self.comment)
            return render(request, self.template_name, {"form": form})


    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST, instance=self.comment)
        if form.is_valid():
            form.save()
            return redirect (self.comment.article.get_absolute_url())
        return  render(request, self.template_name, {"article": self.comment.article, "form": form})
# END