from django import forms
from django.utils.translation import gettext_lazy as _

from ckeditor.widgets import CKEditorWidget
from auction.models import ProductModel

class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorWidget())
    class Meta:
        fields = ('description',)
        model = ProductModel