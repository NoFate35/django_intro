from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from hexlet_django_blog.article.models import Article

from django.contrib import messages

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

from  hexlet_django_blog.article.forms import ArticleCommentForm, ArticleForm


class CommentArticleView(View):
    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            form.save()
                    
    def get(self, request, *args, **kwargs):
        form = ArticleCommentForm()
        return render(request, "articles/comment_form.html", {"form": form})

class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, "articles/create.html", {"form": form})
    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "CREATE!!!")
            return redirect('articles')
        return render(request, 'articles/create.html', {'form': form})
    
class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request, "articles/update.html", {"form": form, "article_id": article_id}
        )
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "UPDATE!!!")
            return redirect("articles")
        return render(request, "articles/update.html", {"form": form, "article_id": article_id})


class ArticleFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect("articles")