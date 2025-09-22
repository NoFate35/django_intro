from django import forms

from .models import Article


# BEGIN (write your solution here)
class ArticleForm(forms.ModelForm):
    model = Article
    fields = ["title", "content"]
# END
