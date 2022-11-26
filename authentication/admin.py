from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from authentication.models import CustomUser

# Register your models here.
# Lop quan tri vien danh cho User - Custom User Translation Admin
@admin.register(CustomUser)
class CustomUserTransAdmin(TranslationAdmin):
    list_display = ('get_username', 'email', 'user_type')
    fields = ('username', 'email', 'user_type', 'is_active', 'is_superuser', 'is_staff')
    # Username field
    @admin.display(ordering='username', description='User Name')
    def get_username(self, obj):
        return obj.username
    # Email field
    @admin.display(ordering='email', description='Email')
    def email(self, obj):
        return obj.email
    # User type : Seller or Buyer
    @admin.display(ordering='user_type', description='User Type')
    def user_type(self, obj):
        return obj.user_type
    
    class Media:
        js = (
            'https://code.jquery.com/jquery-3.6.1.min.js',
            'https://code.jquery.com/ui/1.13.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js'
        )
        css = {
            'screen' : ('modeltranslation/css/tabbed_translation_fields.css',),
        }
