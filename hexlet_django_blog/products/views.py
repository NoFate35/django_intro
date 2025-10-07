from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm
from django.views import View

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        products = Product.objects.all().order_by()
        return render(request, "products/product_list.html", {"products": products,
        'query': query,})

class ProductDetailView(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs["pk"])
        return render(request, "products/product_detail.html", {"product": product})

class CategoryFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = CategoryForm()
        return render(request, "products/category_create.html", {"form": form})
    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        return render(request, 'products/category_create.html', {'form': form})

class ProductFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ProductForm()
        return render(request, "products/product_create.html", {"form": form})
    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
        return render(request, 'products/product_create.html', {'form': form})   