from django.contrib import admin


from .models import *


class ProductsInline(admin.TabularInline):
    model = CategoryProducts.products.through


# Register your models here.
admin.site.register(Dostavka)

admin.site.register(Products)
admin.site.register(Orders)


@admin.register(CategoryProducts)
class CategoryProductsAdmin(admin.ModelAdmin):
    inlines = [ProductsInline]
    exclude = ('products',)

# Register your models here.
