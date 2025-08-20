from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

class IndexView(View):
    def get(self, request, tags, article_id):
        return render(
        request,
        "articles/index.html",
        context={
            "tags": tags,
            "article_id": article_id,
        },
    )

def home_pageView(request):
    return redirect (reverse('article', kwargs={'tags':'python', 'article_id':'42'}) )
