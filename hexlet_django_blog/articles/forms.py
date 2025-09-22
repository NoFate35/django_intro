from django import forms

from .models import Article


# BEGIN (write your solution here)
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content"]
# END
