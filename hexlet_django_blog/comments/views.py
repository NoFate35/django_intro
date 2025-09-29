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
    def get(self, request, *args, **kwargs):
        form = CommentForm()
        return render(request, "comments/comment_form.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
        	print("aaarticle_id", kwargs.get('article_id'))
        	print("aaauthor", form.cleaned_data['author'])
        	print("tttext", form.cleaned_data['text'])
        	#comment = Comment()
        	form.save()
        	return redirect('articles')
        return render(request, "comments/comment_form.html", {"form": form})

class CommentEditView(View):
    def get(self, request, *args, **kwargs):
        form = CommentForm()
        return render(request, "comments/comment_form.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')
        return render(request, "comments/comment_form.html", {"form": form})
# END