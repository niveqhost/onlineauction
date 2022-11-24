from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from django.utils.translation import gettext_lazy as _

from validate_email import validate_email
from utils import constants
# Create your views here.

# ----------------------- Nguoi dung dang ki tai khoan -----------------------
class UserRegister(generic.View):
    template_name = "authentication/register.html"

    def get(self, request, *args, **kwargs):
        try:
            return render(request, self.template_name)
        except Exception as ex:
            print("USER REGISTER GET REQUEST ERROR: ", ex)
    def post(self, request, *args, **kwargs):
        try:
            context = { 'has_error': False, 'data': request.POST }
            #* Xac thuc thong tin dang ki cua nguoi dung
            self.validate_user(request=request, context=context)
            return render(request, self.template_name, context)
        except Exception as ex:
            print("USER REGISTER POST REQUEST ERROR: ", ex)

    #* Xac minh va lam sach thong tin, bao mat thong tin
    def validate_user(self, *args, **kargs):
        #* Lay thong tin nguoi dung nhap vao tu form
        request = kargs.get('request')
        context = kargs.get('context')
        username = request.POST.get('register_username')
        email = request.POST.get('register_email')
        password = request.POST.get('register_password')
        repassword = request.POST.get('register_repassword')
        #* Xac thuc mat khau
        if len(password) < 6:
            messages.add_message(request, constants.MY_MESSAGE_LEVEL, _("Password should be at least 6 characters."), constants.MY_ERROR_TAG)
            context['has_error'] = True
        #* Xac thuc email
        if not validate_email(email):
            messages.add_message(request, constants.MY_MESSAGE_LEVEL, _("Enter a valid email address."), constants.MY_ERROR_TAG)
            context['has_error'] = True
        print(context)
        return context