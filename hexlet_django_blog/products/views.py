from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm, ProductChoiseForm
from django.views import View
from django.views.generic import DetailView, ListView


class ProductListViewPost(View):
	def post(self, request, *args, **kwargs):
		current_category_id = kwargs.get("current_category_id")
		form = kwargs.get("form")
		products = Product.objects.filter(category=current_category_id)
		categories = Category.objects.all()
		return render (request, "products/product_list.html", {"form": form, "products": products, "categories": categories, "current_category_id": current_category_id})


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"
    paginate = 10


    def get(self, request, *args, **kwargs):
        self.category_id = self.kwargs.get("category_id")
        self.form = ProductChoiseForm()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = ProductChoiseForm(self.request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            self.category_id = selection.category.id
            return ProductListViewPost.as_view()(request, **{"form": form, "current_category_id": self.category_id})

    def get_queryset(self):
        category_id = self.__dict__.get('category_id')
        if category_id:
            return Product.objects.filter(category=category_id)
        return Product.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["current_category_id"] = self.__dict__.get('category_id')
        context['form'] = self.form
        return context


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


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "products/product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["current_category_id"] = self.object.category.id
        return context
    