# Generated by Django 4.0.2 on 2023-02-28 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/product_cover', verbose_name='Product image'),
        ),
    ]
