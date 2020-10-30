from django.shortcuts import render, get_object_or_404

from .models import Products, Category

# Create your views here.
def index(request):
    products = Products.objects.all()
    context = {
        'products': products,
        'title': 'List of products',
    }
    return render(request, 'products/index.html', context=context)

def get_category(request, category_id):
    products = Products.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'products/category.html', {'products': products, 'categories': categories, 'category': category})