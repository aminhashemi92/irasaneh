from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, Company
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('phone', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone', 'password1', 'password2'),
        }),
    )
    list_display = ('phone', 'first_name', 'last_name', 'is_staff')
    search_fields = ('phone', 'first_name', 'last_name')
    ordering = ('phone',)


admin.site.register(get_user_model(), CustomUserAdmin)



class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company','role', 'position','pic_tag')
    ordering = ['user', 'company']
    list_filter = ('role', 'position')
    search_fields = ('company','user',)

admin.site.register(Profile,ProfileAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo_tag')
    list_filter = ('name',)
    ordering = ['name', ]
    search_fields = ('name',)

admin.site.register(Company,CompanyAdmin)
