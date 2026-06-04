from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser


class CustomUserAdmin(BaseUserAdmin):
    list_display = ['email', 'name', 'user_type', 'created_at']
    list_filter = ['user_type', 'created_at']
    search_fields = ['email', 'name']
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('name', 'user_type', 'phone', 'bio', 'company_name')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
