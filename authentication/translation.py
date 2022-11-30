from authentication.models import CustomUser, ProfileModel
from modeltranslation.translator import TranslationOptions, register

@register(CustomUser)
class CustomUserTranslationOptions(TranslationOptions):
    fields = (
        'user_type',
    )

@register(ProfileModel)
class ProfileModelTranslationOptions(TranslationOptions):
    fields = (
        'gender',
    )