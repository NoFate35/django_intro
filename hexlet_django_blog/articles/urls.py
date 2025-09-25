from django.urls import path

from . import views

# BEGIN (write your solution here)
urlpatterns = [
    path("", views.ArticleListView.as_view(), name="article_list"),
    path("<int:id>/update/", views.ArticleFormUpdateView.as_view(), name="article_update"),
    path("<int:id>/delete/", views.ArticleFormDeleteView.as_view(), name="article_delete"),
    path("<int:id>/", views.ArticleDetailView.as_view(), name="article_detail"),
    path("create/", views.ArticleFormView.as_view(), name="article_create"),

    # END
]
