from django.contrib.auth import get_user_model
from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
from django.utils import timezone


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(verbose_name=_('Product image'), upload_to='product/product_cover', blank=True)
    # image = models.ImageField(verbose_name=_('Product image'), upload_to='product/product_cover', blank=False)
    active = models.BooleanField(default=True)
    # datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_created = models.DateTimeField(verbose_name=_('product_create_date'), default=timezone.now)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.id])


class Comments(models.Model):
    Product_STARS = (
        ('1', _('VeryBad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Prefect')),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comments',
                               verbose_name=_('Comment author'))
    body = RichTextField(verbose_name=_('Text'))
    stars = models.CharField(max_length=10, choices=Product_STARS, verbose_name=_('Point'))
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.product.id])
