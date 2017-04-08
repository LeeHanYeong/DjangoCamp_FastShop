from django.contrib import admin

from product.models import Category, Product, DateRangeDiscount

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(DateRangeDiscount)
