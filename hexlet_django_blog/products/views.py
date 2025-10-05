from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views import View

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        products = Product.objects.all().order_by()
        return render(request, "products/product_list.html", {"products": products,
        'query': query,})

class ArticleDetailView(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs["id"])
        return render(request, "products/products_detail.html", {"product": product})
