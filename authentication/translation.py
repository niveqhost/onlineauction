from authentication.models import CustomUser
from modeltranslation.translator import TranslationOptions, register

@register(CustomUser)
class CustomUserTranslationOptions(TranslationOptions):
    fields = (
        'user_type',
    )