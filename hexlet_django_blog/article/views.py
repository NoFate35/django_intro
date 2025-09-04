from django.shortcuts import render, get_object_or_404
from django.views import View

from hexlet_django_blog.article.models import Article

class IndexView(View):
    def get(self, request):
        articles = Article.objects.all()[:15]
        print('artiiicles', articles)
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article_name = kwargs["name"]
        print('article_name', article_name)
        article = get_object_or_404(Article, name=article_name)
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )

from  hexlet_django_blog.article.forms import ArticleCommentForm
from  hexlet_django_blog.article.models import ArticleComment


class CommentArticleView(View):
    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
        	form.save()

    def get(self, request, *args, **kwargs):
        form = ArticleCommentForm()
        return render(
            request, "articles/comment_form.html", {"form": form}
        )