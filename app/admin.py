from django.contrib import admin
from .models import *


@admin.register(PartnerApplication)
class AdminUser(admin.ModelAdmin):
    list_display = 'id', 'app_type', 'company_name', 'full_name', 'phone'


@admin.register(PartnerApplicationObjectImage)
class AdminNew(admin.ModelAdmin):
    list_display = 'id', 'file', 'application',


@admin.register(Location)
class AdminBranch(admin.ModelAdmin):
    list_display = 'id', 'address', 'description', 'region'


@admin.register(PartnerApplicationObject)
class AdminCertificate(admin.ModelAdmin):
    list_display = 'id', 'type',


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone')


@admin.register(UserLocation)
class AdminUserLocation(admin.ModelAdmin):
    list_display = ('id', 'lat', 'lon', 'address', 'user')


@admin.register(UserCard)
class AdminUserCard(admin.ModelAdmin):
    list_display = 'id',


@admin.register(Vacancy)
class AdminVacancy(admin.ModelAdmin):
    list_display = 'id',


@admin.register(VacancyApplication)
class AdminVacancyApplication(admin.ModelAdmin):
    list_display = 'id',


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ('id', 'name', 'order')
    ordering = ['order']


@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'description', 'price', 'discount_price', 'category')


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = 'id',


@admin.register(OrderProduct)
class AdminOrderProduct(admin.ModelAdmin):
    list_display = 'id',


@admin.register(Branch)
class AdminBranch(admin.ModelAdmin):
    list_display = ('id', 'name', 'order', 'duration', 'address', 'lon', 'lat')
    list_filter = ('name', )


@admin.register(Career)
class AdminCareer(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(New)
class AdminNew(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'order', 'created_at')


@admin.register(FAQ)
class AdminFAQ(admin.ModelAdmin):
    list_display = ('id', 'question', 'answer')


@admin.register(Feedback)
class AdminFeedback(admin.ModelAdmin):
    list_display = ('id', 'full_name')


@admin.register(UserEmail)
class AdminUserEmail(admin.ModelAdmin):
    list_display = ('id', 'email')


@admin.register(AboutUs)
class AdminAboutUS(admin.ModelAdmin):
    list_display = ('id', 'key', 'value')


@admin.register(Certificate)
class AdminCertificate(admin.ModelAdmin):
    list_display = 'id',