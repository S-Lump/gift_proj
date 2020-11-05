from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Products, Category


# class Home(ListView):
#     model = Products
#     template_name = 'products/category.html'
#     context_object_name = 'categories'
#     # extra_content = {
#     #     'title': 'Главная',
#     # }
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Главная'




class Home(ListView):
    model = Category
    template_name = 'products/index.html'
    context_object_name = 'categories'


def get_category(request, category_id):
    products = Products.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    return render(request, 'products/category.html', {'products': products, 'categories': categories, 'category': category})


class Product(DetailView):
    model = Products
    template_name = 'products/detail.html'
    context_object_name = 'product'
    
    # def get_queryset(self, slug):
    #     return Products.objects.get(slug=slug)