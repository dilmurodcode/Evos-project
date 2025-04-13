from django.contrib import admin
from .models import *


@admin.register(PartnerApplication)
class AdminUser(admin.ModelAdmin):
    list_display = 'id', 'type', 'company_name', 'full_name', 'phone'


@admin.register(PartnerApplicationObjectImage)
class AdminNew(admin.ModelAdmin):
    list_display = 'id', 'file', 'application',


@admin.register(Location)
class AdminBranch(admin.ModelAdmin):
    list_display = 'id', 'address', 'description', 'region'


@admin.register(PartnerApplicationObject)
class AdminCertificate(admin.ModelAdmin):
    list_display = 'id', 'type',