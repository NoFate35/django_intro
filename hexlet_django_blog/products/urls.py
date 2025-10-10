from django.urls import path

from hexlet_django_blog.products import views

urlpatterns = [
    path("", views.ProductListView.as_view(), name='product_list'),
    path("category/<int:category_id>/", views.ProductListView.as_view(), name='product_by_category'),
    path("category/create/", views.CategoryFormCreateView.as_view(), name='category_create'),
    path("create/", views.ProductFormCreateView.as_view(), name='product_create'),
    path("<int:pk>/", views.ProductDetailView.as_view(), name='product_detail'),
]