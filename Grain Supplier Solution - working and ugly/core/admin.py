from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models



@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    list_display = ['id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']
    list_filter = ('is_staff', 'is_active',)
    list_editable = ['is_staff', 'is_active']
    search_fields = ['email__istartswith', 'first_name__istartswith', 'last_name__istartswith']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2',),
        }),
    )
    ordering = ('first_name', 'last_name',)
    list_per_page = 10
