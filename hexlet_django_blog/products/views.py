from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm, ProductChoiseForm
from django.views import View

class ProductListView(View):
    def get(self, request, *args, **kwargs):
        category_id = kwargs.get("category_id")
        
        form = ProductChoiseForm()
        if not category_id:
            products = Product.objects.all()
        else:
            products = Product.objects.filter(category=category_id)
        return render(request, "products/product_list.html", {"products": products, 'form': form})
 
    def post(self, request, *args, **kwargs):
        form = ProductChoiseForm(request.POST)
        category_id = form.save(commit=False)
        category_filter = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category_filter)
        return render(request, "products/product_list.html", {"products": products, 'form': form})


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