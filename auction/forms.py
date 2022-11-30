from django import forms
from django.utils.translation import gettext_lazy as _

from ckeditor.widgets import CKEditorWidget
from auction.models import *

class ProductForm(forms.ModelForm):
    # Ten san pham
    product_name = forms.CharField(max_length=200,
        widget = forms.TextInput(
            attrs = {
                'placeholder' : _('Enter your product name'),
                'class' : 'mb-2 col-xl-11 col-lg-11'
            })
        )
    # Mo ta san pham
    description = forms.CharField(
        widget=CKEditorWidget(
            attrs = {
                'placeholder' : _('Enter your product description'),
            })
        )
    # Danh muc san pham
    # Gia thap nhat
    class Meta:
        model = ProductModel
        fields = ('product_name', 'description',)

class ImageForm(forms.ModelForm):
    # Anh san pham
    product_images = forms.ImageField(
        label=_("Select Images"),
        widget=forms.ClearableFileInput(
            attrs={
                'multiple' : True,
                'style' : 'padding: 12px'
            }
        )
    )
    class Meta:
        model = ProductImage
        fields = ('product_images',)
