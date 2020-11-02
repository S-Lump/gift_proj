from django.db import models
from django.urls import reverse_lazy


class Products(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateField(auto_now=True, verbose_name='Обновлено')
    photo = models.ImageField(upload_to='photos/', verbose_name='Изображение')
    slug = models.SlugField(unique=True, verbose_name='Слаг')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, blank=True, null=True)

    def get_absolute_url(self):
        return reverse_lazy('products', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse_lazy('category', kwargs={'category_id': self.pk})

    def __str__(self): 
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'



