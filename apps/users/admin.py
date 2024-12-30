from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser  # Replace 'CustomUser' with the name of your user model

@admin.register(CustomUser)
class CustomUserAdmin(BaseUserAdmin):
    # Fields to display in the admin form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),  # Add custom fields here
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    
    # Fields for the add user form
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2'),  # Include custom fields
        }),
    )
    
    # Columns to display in the list view
    list_display = ('email', 'first_name', 'last_name','is_staff', 'is_superuser')
    
    # Searchable fields
    search_fields = ('email', 'first_name', 'last_name')
    
    # Default ordering for the list view
    ordering = ('email',)
