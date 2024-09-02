from django.contrib import admin

from django.contrib.admin import register

from catalouge.models import Brand, Category, Product, ProductAttribute, ProductType, ProductAttributeValue

@register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    pass


@register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    pass


@register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    pass
