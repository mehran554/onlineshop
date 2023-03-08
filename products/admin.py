from django.contrib import admin
from django.utils.safestring import mark_safe
# from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin
from .models import Product, Comments


class CommentsInline(admin.TabularInline):
    model = Comments
    fields = ['author', 'body', 'stars', 'active']
    extra = 0


class AdminProduct(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'datetime_created', 'active']
    inlines = [CommentsInline, ]


admin.site.register(Product, AdminProduct)


# @admin.register(Comments)
class AdminComment(admin.ModelAdmin):
    list_display = ['product', 'safe_text', 'author', 'stars', 'active', 'datetime_create', ]

    @admin.display()  # برای در هم نریختن کاراکترهای کامنت ها در پنل ادمین
    def safe_text(self, obj):
        return mark_safe(obj.body)  # Note:  نام فیلد اصلی موجود در فایل مدل ما میباشد body


admin.site.register(Comments, AdminComment)
