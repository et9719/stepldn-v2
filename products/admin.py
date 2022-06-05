''' Imports '''
from django.contrib import admin
from .models import Product, Category, Review


class ProductAdmin(admin.ModelAdmin):
    ''' Define what the site owner should see
    on the products part of the admin page '''
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    ''' Define what admin should see in category part of admin page '''
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    ''' what admoin should see, how it can be filtered
    what you can search and action to approve reviews'''
    list_display = ('name', 'body', 'product', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_reviews']

    def approve_reviews(self, request, queryset):
        ''' if approved by admin update active to true '''
        queryset.update(active=True)
