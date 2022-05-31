''' Imports '''
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin, SummernoteModelAdmin):
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

    summernote_fields = ('description')


class CategoryAdmin(admin.ModelAdmin):
    ''' Define what admin should see in category part of admin page '''
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
