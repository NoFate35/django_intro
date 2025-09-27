from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.decorators import method_decorator
from django.views import View

from hexlet_django_blog.articles.models import Article
from hexlet_django_blog.comments.models import Comment

from .forms import CommentForm


# BEGIN (write your solution here)

# END