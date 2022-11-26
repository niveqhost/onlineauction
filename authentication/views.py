from django.conf import settings
from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth import authenticate, login, logout
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from utils import constants
from validate_email import validate_email
from authentication.models import CustomUser
from utils.send_mail_util import generate_token

# Create your views here.
# ----------------------- Nguoi dung dang ki tai khoan -----------------------
class RegisterUser(generic.View):
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
            if context['has_error']:
                return render(request, self.template_name, context)
            #* Neu thong tin dang ki la hop le thi tao tai khoan cho nguoi dung
            user = CustomUser.objects.create_user(username=request.POST.get('register_username'), email=request.POST.get('register_email'))
            user.set_password(request.POST.get('register_password'))
            user.save()
            #* Gui email yeu cau kich hoat tai khoan
            if not context.get('has_error'):
                self.send_activation_email(user, request)
                messages.add_message(request, constants.MY_MESSAGE_LEVEL, 'We sent you an email to verify your account.', constants.MY_INFO_TAG)
                context.pop('data')
            return render(request, self.template_name, context)
        except Exception as ex:
            print("USER REGISTER POST REQUEST ERROR: ", ex)

    #* Xac minh va lam sach thong tin, bao mat thong tin
    def validate_user(self, *args, **kargs) -> dict:
        #* Lay thong tin nguoi dung nhap vao tu form
        request = kargs.get('request')
        context = kargs.get('context')
        username = request.POST.get('register_username')
        email = request.POST.get('register_email')
        password = request.POST.get('register_password')
        repassword = request.POST.get('register_repassword')
        #* Ten, email, mat khau khong duoc de trong
        if username == "" or email == "" or password == "" or repassword == "":
            messages.add_message(request, constants.MY_MESSAGE_LEVEL ,_("All fields are required."), constants.MY_ERROR_TAG)
            context['has_error'] = True
        # TODO: Xac thuc ten nguoi dung: Ten nguoi dung khong chua ki tu dac biet
        #* Xac thuc mat khau: Mat khau phai co do dai lon hon 8 ki tu
        if len(password) < 8:
            messages.add_message(request, constants.MY_MESSAGE_LEVEL, _("Password should be at least 8 characters."), constants.MY_ERROR_TAG)
            context['has_error'] = True
        #* Xac thuc mat khau: Mat khau va nhap lai mat khau phai trung nhau
        if password != repassword:
            messages.add_message(request, constants.MESSAGE_EXTRA_LEVEL ,_("Password and confirm password don't match."), constants.MESSAGE_ERROR_TAGS)
            context['has_error'] = True
        #* Xac thuc email
        if not validate_email(email):
            messages.add_message(request, constants.MY_MESSAGE_LEVEL, _("Enter a valid email address."), constants.MY_ERROR_TAG)
            context['has_error'] = True
        #* Kiem tra xem ten nguoi dung da co trong co so du lieu hay chua
        if CustomUser.objects.filter(username=username).exists():
            messages.add_message(request, constants.MY_MESSAGE_LEVEL ,_("Username is already exist. Please try some other username."), constants.MY_ERROR_TAG)
            context['has_error'] = True
        #* Kiem tra xem dia chi email da co trong co so du lieu hay chua
        if CustomUser.objects.filter(email=email).exists():
            messages.add_message(request, constants.MY_MESSAGE_LEVEL ,_("This email address is already used."), constants.MY_ERROR_TAG)
            context['has_error'] = True
        return context

    #* Gui email yeu cau kich hoat tai khoan
    def send_activation_email(self, user, request) -> None:
        current_site = get_current_site(request)
        email_subject = 'Kích hoạt tài khoản của bạn'
        from_email = 'cskh@hotro.sbidu.vn'
        recipient_email = request.POST.get('register_email')
        email_message = 'Cảm ơn quý khách đã sử dụng dịch vụ.'
        context = {
            'user': user, # Nguoi dung
            'domain': current_site, # Ten mien trang web
            # uid: User ID - Ma hoa id cua nguoi dung
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            # Tao ma token dung de kich hoat tai khoan nguoi dung
            'token': generate_token.make_token(user)
        }
        email_body = render_to_string('authentication/activate.html', context)
        send_mail(subject=email_subject,message=email_message, from_email=from_email, recipient_list=[recipient_email], fail_silently=False, html_message=email_body)

# ---------------- Kich hoat tai khoan cua nguoi dung qua email ----------------
class ActivateUser(generic.View):
    activate_fail_template = 'authentication/activate-failed.html'

    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(pk=uid)
        except Exception as ex:
            print("ACTIVATE USER METHOD ERROR: ", ex)
            user = None
        if user and generate_token.check_token(user, token):
            # Nguoi dung da xac thuc email tai khoan
            user.is_email_verified = True
            # Kich hoat tai khoan cho nguoi dung
            user.is_active = True
            user.save()
            # Kich hoat thanh cong, thong bao cho nguoi dung va quay ve trang dang nhap
            messages.add_message(request, constants.MY_MESSAGE_LEVEL, _('Your email is verified. You can now login.'), constants.MY_SUCCESS_TAG)
            return redirect(reverse('authentication:login'))
        # Kich hoat tai khoan that bai hoac co loi xay ra
        return render(request, self.activate_fail_template, {"user": user})

# ----------------------- Nguoi dung dang nhap tai khoan -----------------------
class LoginUser(generic.View):
    template_name = "authentication/login.html"
    def get(self, request):
        try:
            return render(request, self.template_name)
        except Exception as ex:
            print('LOGIN USER GET REQUEST ERROR: ', ex)
    def post(self, request):
        try:
            username = request.POST.get('login_username')
            password = request.POST.get('login_password')
            #* Xac thuc tai khoan hop le
            user = authenticate(request, username=username, password=password)
            if user is not None:
                #* Dang nhap thanh cong, dieu huong ve trang chu
                login(request, user)
                messages.add_message(request, constants.MY_MESSAGE_LEVEL, _('You have logged in successfully.'), constants.MY_SUCCESS_TAG)
                return redirect('auction:index')
            return render(request, self.template_name)
        except Exception as ex:
            print('LOGIN USER GET REQUEST ERROR: ', ex)

# ----------------------- Nguoi dung dang xuat tai khoan -----------------------
class LogoutUser(generic.View):
    @method_decorator(login_required)
    def get(self, request):
        try:
            #* Dang xuat thanh cong
            logout(request)
            messages.add_message(request, constants.MY_MESSAGE_LEVEL, _('You logged out successfully.'), constants.MY_SUCCESS_TAG)
            return redirect('authentication:login')
        except Exception as ex:
            print('LOGOUT USER GET REQUEST ERROR: ', ex)

# -------------------- Quan li thong tin, tai khoan ca nhan --------------------
class ViewProfile(generic.View):
    template_name = 'authentication/profile.html'
    @method_decorator(login_required)
    # def get(self, request, user_id, *args, **kwargs):
    def get(self, request, *args, **kwargs):
        try:
            # user = CustomUser.objects.get(id=user_id)
            # context = {
            #     "user": user
            # }
            return render(request, self.template_name)
        except Exception as ex:
            print('PROFILE VIEW GET REQUEST ERROR: ', ex)