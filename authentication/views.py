from django.shortcuts import render
from django.views import generic
from django.utils.translation import gettext_lazy as _

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
            context = {'has_error': False, 'data': request.POST}
            # * Lay thong tin nguoi dung nhap vao tu form
            username = request.POST.get('register_username')
            email = request.POST.get('register_email')
            password = request.POST.get('register_password')
            repassword = request.POST.get('register_repassword')
            # * Xac minh va lam sach thong tin, bao mat thong tin
            self.user_validation(username=username, email=email, password=password, repassword=repassword)
        except Exception as ex:
            print("USER REGISTER POST REQUEST ERROR: ", ex)

    # * Xac minh va lam sach thong tin, bao mat thong tin
    def user_validation(self, *args, **kargs):
        print(kargs.get("username"))