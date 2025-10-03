from django.urls import path

from hexlet_django_blog.products import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name='product_list'),
]