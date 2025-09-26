from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from .forms import ArticleForm
from .models import Article


class ArticleListView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all().order_by("-created_at")
        return render(request, "articles/list.html", {"articles": articles})


class ArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(request, "articles/detail.html", {"article": article})


# BEGIN (write your solution here)

class ArticleFormView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, "articles/form.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('article_list')

class ArticleFormUpdateView(View):
     def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        form = ArticleForm(instance=article)
        return render(
            request, "articles/form.html", {"form": form} )
     def post(self, request, *args, **kwargs):
         article = get_object_or_404(Article, id=kwargs["id"])
         form = ArticleForm(request.POST, instance=article)
         if form.is_valid():
             form.save()
             return redirect("article_list")
         return render(request, "articles/form.html", {"form": form})

class ArticleFormDeleteView(View):
    def get (self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        if article:
           return render(request, "articles/article_confirm_delete.html", {"article": article})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
        return redirect("article_list")
# END
