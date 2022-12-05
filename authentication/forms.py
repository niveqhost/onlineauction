from django import forms
from django.utils.translation import gettext_lazy as _

from authentication.models import CustomUser

# Create a user form
class CustomUserForm(forms.ModelForm):
    username = forms.CharField(
        label= '',
        widget = forms.TextInput(
            attrs = {
                'placeholder' : _('Enter User Name'), 
                'autocomplete' : "off",
                'class' : "form-group mb-30"
            }),
        error_messages = {
            'required': 'Please enter user name.'
        }
    )
    email = forms.CharField(
        label= '',
        widget = forms.TextInput(
            attrs = {
                'placeholder' : _('Enter your email'), 
                'autocomplete' : "off",
                'type' : 'email',
                'class' : "form-group mb-30"
            }),
        error_messages = {
            'required': 'Please enter your email.'
        }
    )
    password = forms.CharField(
        label= '',
        widget = forms.TextInput(
            attrs = {
                'placeholder' : _('Enter your password'), 
                'autocomplete' : "off",
                'type' : 'password',
                'class' : "form-group mb-30"
            }),
        error_messages = {
            'required': 'Please enter your email.'
        }
    )
    repassword = forms.CharField(
        label= '',
        widget = forms.TimeInput(
            attrs = {
                'placeholder' : _('Enter your confirm password'), 
                'autocomplete' : "off",
                'type' : 'password',
                'class' : "form-group mb-30"
            }),
        error_messages = {
            'required': 'Please enter your confirm password.'
        }
    )

    class Meta:
        fields = ('username', 'email', 'password',)
        model = CustomUser