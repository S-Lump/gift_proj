from django.urls import path 

from .views import *

urlpatterns = [
    path('register/', user_register, name='register'),

    path('login/', user_login, name='login'),
    path('cart/', get_cart(), name='cart'),
    path('logout/', user_logout, name='logout'),
    path('', Home.as_view(), name='home'),
    path('category/<int:category_id>', get_category, name='category'),
    path('products/<str:slug>', Product.as_view(), name='products')
]
