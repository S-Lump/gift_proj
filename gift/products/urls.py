from django.urls import path 

from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<int:category_id>', get_category, name='category')
]
