from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from authentication.models import *
from authentication.forms import *

# Register your models here.
# Lop quan tri vien danh cho User - Custom User Translation Admin
@admin.register(CustomUser)
class CustomUserTransAdmin(TranslationAdmin):
    list_display = ('get_username', 'email', 'user_type')
    fields = ('username', 'email', 'user_type', 'is_active', 'is_superuser', 'is_staff', 'avatar')

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

# Lop quan tri vien danh cho ho so nguoi dung - Profile Model Translation Admin
@admin.register(ProfileModel)
class ProfileModelTransAdmin(TranslationAdmin):
    list_display = ('full_name', 'date_of_birth', 'address')
    fields = ('full_name', 'phone_number', 'date_of_birth', 'address', 'gender', 'user')
    # Ho va ten
    @admin.display(ordering='full_name', description='Full Name')
    def full_name(self, obj):
        return obj.full_name
    # Ngay, thang, nam sinh
    @admin.display(ordering='date_of_birth', description='Date of Birth')
    def date_of_birth(self, obj):
        return obj.date_of_birth
    # Dia chi
    @admin.display(ordering='address', description='Address')
    def address(self, obj):
        return obj.address
    
    class Media:
        js = (
            'https://code.jquery.com/jquery-3.6.1.min.js',
            'https://code.jquery.com/ui/1.13.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js'
        )
        css = {
            'screen' : ('modeltranslation/css/tabbed_translation_fields.css',),
        }
