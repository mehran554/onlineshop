from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    # model = CustomUser
    model = get_user_model()
    list_display = ['email', 'username', ]
    # fieldsets =
    # add_fieldsets =


admin.site.register(CustomUser, CustomUserAdmin)
