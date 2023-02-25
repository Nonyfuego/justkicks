from django.contrib import admin
from .models import Product, Category, FootwearType, Brand

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','brand','color','size','date_added')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

class FootwearTypeAdmin(admin.ModelAdmin):
    list_display = ('title',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(FootwearType, FootwearTypeAdmin)
admin.site.register(Brand, BrandAdmin)