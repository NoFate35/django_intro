from django.urls import path

from . import views

urlpatterns = [
    path("", views.ArticleListView.as_view(), name="article_list"),
    path("<int:id>/", views.ArticleDetailView.as_view(), name="article_detail"),
    # BEGIN (write your solution here)
    path("create/", views.ArticleFormView.as_view(), name="article_create")
    # END
]
