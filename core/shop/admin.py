from django.contrib import admin
from .models import Product, ProductImage, ProductCategory


# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "stock", "status","price","discount_percent", "created_date")

@admin.register(ProductCategory)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_date")

@admin.register(ProductImage)
class ProductImageModelAdmin(admin.ModelAdmin):
    list_display = ("id", "file", "created_date")

# @admin.register(WishlistProductModel)
# class WishlistProductModelAdmin(admin.ModelAdmin):
#     list_display = ("id", "user", "product")

