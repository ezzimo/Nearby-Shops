from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import User
from .models import Shop
from .views import home
from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos

# Register your models here.




@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    """Define admin model for custom User model with no email field."""

    fieldsets = (
        (None, {'fields': ('email', 'location', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'maplocation')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'location', 'maplocation', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'location', 'maplocation', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

#admin.site.register(Shop)

class ShopAdmin(admin.ModelAdmin):
     list_display =('name', 'city', 'email', 'shop_pic')
     pass

# Register the admin class wuth the model
admin.site.register(Shop, ShopAdmin)
