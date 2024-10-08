from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'is_dm']


admin.site.register(CustomUser, CustomUserAdmin)
