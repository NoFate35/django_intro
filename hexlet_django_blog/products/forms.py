from django import forms

from .models import Product, Category


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "category"]

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]