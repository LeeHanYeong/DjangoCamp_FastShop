from django.contrib import admin
from django.urls import reverse

from product.models import Category, Product, DateRangeDiscount


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'full_title',
        'priority',
    )
    list_filter = (
        'parent',
    )


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'admin_categories',
        'price',
    )

    def admin_categories(self, obj):
        ret = ''
        for category in obj.categories.all():
            admin_url = reverse('admin:product_category_change', args=(category.id,))
            ret += '- <a href="{}">{}</a><br>'.format(
                admin_url,
                category.full_title
            )
        return ret

    admin_categories.allow_tags = True


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(DateRangeDiscount)
