from django.shortcuts import render
from django.views import generic
from django.utils.translation import gettext_lazy as _

# Create your views here.
# Nguoi dung dang ki tai khoan
class UserRegister(generic.View):
    template_name = "authentication/register.html"
    def get(self, request):
        try:
            return render(request, self.template_name)
        except Exception as ex:
            print("USER REGISTER GET REQUEST ERROR: ", ex)
    def post(self, request):
        try:
            pass
        except Exception as ex:
            print("USER REGISTER POST REQUEST ERROR: ", ex)