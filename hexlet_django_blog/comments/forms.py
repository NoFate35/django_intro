from django import forms

from .models import Comment


# BEGIN (write your solution here)
from django.forms import ModelForm
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["author", "text"]
        widgets = {
            "text": forms.Textarea(attrs={"rows": 3}),
        }
    def clean_text(self):
        text = self.cleaned_data["text"]
        if len(text.strip()) == 0:
            raise forms.ValidationError("Comment text cannot be empty!")
        return text
# END