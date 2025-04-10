from django.contrib import admin
from .models import *


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = 'id', 'number', 'is_active'
    list_display_links = 'id', 'number', 'is_active'


@admin.register(New)
class AdminNew(admin.ModelAdmin):
    list_display = 'title', 'description'
    list_display_links = 'title', 'description'


@admin.register(Branch)
class AdminBranch(admin.ModelAdmin):
    list_display = 'name', 'address', 'start_work', 'end_work'
    list_display_links = 'name', 'address', 'start_work', 'end_work'


@admin.register(Certificate)
class AdminCertificate(admin.ModelAdmin):
    list_display = 'description', 'order'
    list_display_links = 'description', 'order'


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = 'name',
    list_display_links = 'name',


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = 'title', 'price', 'category'
    list_display_links = 'title', 'price', 'category'