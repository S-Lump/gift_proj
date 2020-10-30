from django.contrib import admin
from .models import Products, Category


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'photo', 'price')

admin.site.register(Products, ProductsAdmin)
admin.site.register(Category)