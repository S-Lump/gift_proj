# Generated by Django 3.1.4 on 2020-12-16 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201030_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/', verbose_name='Изображение'),
        ),
    ]
