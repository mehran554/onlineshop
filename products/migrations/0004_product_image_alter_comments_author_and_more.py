# Generated by Django 4.0.2 on 2023-02-28 15:13

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0003_alter_comments_stars'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/product_cover', verbose_name='Product image'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='نظر نویسنده'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='متن دیدگاه'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='stars',
            field=models.CharField(choices=[('1', 'خیلی بد'), ('2', 'بد'), ('3', 'معمولی'), ('4', 'خوب'), ('5', 'عالی')], max_length=10, verbose_name='امتیاز'),
        ),
    ]