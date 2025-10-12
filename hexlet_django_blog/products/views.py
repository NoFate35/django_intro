from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm, ProductChoiseForm
from django.views import View
from django.views.generic import DetailView, ListView

class ProductListView(ListView):
    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"
    paginate = 10

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.category_id = self.kwargs.get("category_id")
        self.form = ProductChoiseForm()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = ProductChoiseForm(self.request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            self.category_id = selection.category.id
            self.form = form
            return super().post(request, *args, **kwargs)

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
    
    '''

    def get(self, request, *args, **kwargs):
        category_id = kwargs.get("category_id")
        form = ProductChoiseForm()
        categories = Category.objects.all()
        if not category_id:
            products = Product.objects.all()
        else:
            products = Product.objects.filter(category=category_id)
        return render(request, "products/product_list.html", {"products": products, 'form': form, 'categories': categories, 'current_category_id': category_id})
 
    def post(self, request, *args, **kwargs):
        form = ProductChoiseForm(request.POST)
        if form.is_valid():
            selection = form.save(commit=False)
            category_for_filter = get_object_or_404(Category, id=selection.category.id)
            products = Product.objects.filter(category=category_for_filter)
            return render(request, "products/product_list.html", {"products": products, 'form': form})
'''

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
    
    '''
class ProductListView(ListView):
    model = Product
    context_object_name = "products"
    template_name = "product_list.html"
    paginate = 10

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        if category_id:
            self.category = get_object_or_404(Category, id=category_id)
            return Product.objects.filter(category=self.category)
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["current_category_id"] = self.kwargs.get("category_id")
        return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = "product"
    template_name = "product_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["current_category_id"] = self.object.category.id
        return context
    '''