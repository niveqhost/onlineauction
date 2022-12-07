from django.contrib import admin
from django.utils.html import format_html
from modeltranslation.admin import TranslationAdmin

from auction.models import *
from auction.forms import *

# Register your models here.

@admin.register(CategoryModel)
class CategoryTransAdmin(TranslationAdmin):
    list_display = ('id', 'category_name',)
    fields = ('category_name', 'category_image', 'category_slug',)

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
    list_display = ('product_name', 'get_thumbnail',)

    @admin.display(ordering='product_name', description='Product Name')
    def product_name(self, obj):
        return obj.product_name

    @admin.display(ordering='thumbnail', description='Product Thumbnail')
    def get_thumbnail(self, obj):
        return format_html(f'<img src="{obj.thumbnail.url}"style="height:100px; width=100px;">')
    
    class Meta:
        form = ProductForm

@admin.register(ProductImage)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('product_photos',)

    @admin.display(ordering='product_images', description='Product Images')
    def product_photos(self, obj):
        return format_html(f'<img src="{obj.product_images.url}" style="height:100px; width=100px;">')

    class Meta:
        form = ImageForm