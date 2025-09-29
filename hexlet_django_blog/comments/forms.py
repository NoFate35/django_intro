from django import forms

from .models import Comment


# BEGIN (write your solution here)
from django.forms import ModelForm
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["author", "text"]
# END