from auction.models import CategoryModel
from modeltranslation.translator import TranslationOptions, register

@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = (
        'category_name',
    )