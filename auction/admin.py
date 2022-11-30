from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from auction.models import *
from auction.forms import *

# Register your models here.

@admin.register(CategoryModel)
class CategoryTransAdmin(TranslationAdmin):
    list_display = ('id', 'category_name',)
    fields = ('category_name',)

    # Ma danh muc
    @admin.display(ordering='id', description='Category ID')
    def id(self, obj):
        return obj.id

    # Ten danh muc
    @admin.display(ordering='category_name', description='Category Name')
    def category_name(self, obj):
        return obj.category_name
    
    class Media:
        js = (
            'https://code.jquery.com/jquery-3.6.1.min.js',
            'https://code.jquery.com/ui/1.13.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js'
        )
        css = {
            'screen' : ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(ProductModel)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name',)

    @admin.display(ordering='product_name', description='Product Name')
    def product_name(self, obj):
        return obj.product_name

    class Meta:
        form = ProductForm
