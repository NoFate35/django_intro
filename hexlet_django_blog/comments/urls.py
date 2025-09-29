from django.urls import path

from .views import CommentAddView, CommentEditView

# BEGIN (write your solution here)
urlpatterns = [
    path("<int:article_id>/add/", CommentAddView.as_view(), name="comment_add"),
    path("<int:pk>/edit/", CommentAddView.as_view(), name="comment_edit"),
]
# END
