from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout

from .models import Products, Category



# class Home(ListView):
#     model = Products
#     template_name = 'products/category.html'
#     context_object_name = 'categories'
#     # extra_content = {
#     #     'title': 'Главная',
#     # }




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



def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'products/register.html', {"form": form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'products/login.html', {"form": form})

def user_logout(request):
    logout(request)
    return redirect('login')


   # def get_context_data(self, *, object_list=None, **kwargs):
 #        context = super().get_context_data(**kwargs)
  #       context['title'] = 'Товар'

# def get_queryset(self, slug):
    #     return Products.objects.get(slug=slug)