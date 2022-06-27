from django.contrib import admin
from .models import *


# Register your models here.


class c_admin(admin.ModelAdmin):
    prepopulated_fields = {'c_slug': ('c_name',)}


admin.site.register(category, c_admin)


class p_admin(admin.ModelAdmin):
    list_display = ['p_name', 'p_slug', 'p_img', 'p_price', 'p_stock', 'p_available']
    list_editable = ['p_available', 'p_img', 'p_stock', 'p_price']
    prepopulated_fields = {'p_slug': ('p_name',)}


admin.site.register(products, p_admin)
