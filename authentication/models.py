from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.

# Lop CustomerUserManager ke thua tu lop UserManager
class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Invalid Email."))
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, email, password, **extra_fields)

# Lop lien quan den co so du lieu
# Tai khoan khach hang
class CustomUser(AbstractBaseUser, PermissionsMixin):
    # Constant Variable
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    user_choice = (
        ('Seller', 'Seller'),
        ('Buyer', 'Buyer'),
        ('Staff', 'Staff'),
    )
    objects =  CustomUserManager()
    # Ma tai khoan - Tu tao boi he thong
    # Ten tai khoan
    username = models.CharField(max_length=255, null=True, unique=True)
    # Email
    email = models.EmailField(blank=True, unique=True)
    # Quyen quan tri he thong
    is_superuser = models.BooleanField(default=False)
    # Quyen nhan vien he thong
    is_staff = models.BooleanField(default=False)
    # Tai khoan da duoc kich hoat hay chua
    is_active = models.BooleanField(default=False)
    # Tai khoan da xac thuc email hay chua
    is_email_verified = models.BooleanField(default=False)
    # Ngay tao tai khoan
    date_joined = models.DateField(default=timezone.now)
    # Lan dang nhap cuoi
    last_login = models.DateField(blank=True, null=True)
    # Loai tai khoan: Nguoi mua, nguoi ban, nhan vien giao dich
    user_type = models.CharField(max_length = 30, choices = user_choice, default = 'Buyer')
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self) -> str:
        return self.username
    def get_full_name(self):
        return self.username
    def get_short_name(self):
        return self.username or self.email.split('@')[0]

# Ho so khach hang
class ProfileModel(models.Model):
    pass
    # Ma ho so - 1 khach hang chi co 1 ho so
    # Ho va ten
    # So dien thoai
    # Ngay, thang, nam sinh
    # Dia chi
    # Gioi tinh
    # Anh dai dien

# Thong tin lien he
class ContactModel(models.Model):
    pass