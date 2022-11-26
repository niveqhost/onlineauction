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
    username = models.CharField(max_length=255, null=True, unique=True)
    email = models.EmailField(blank=True, unique=True)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    date_joined = models.DateField(default=timezone.now)
    last_login = models.DateField(blank=True, null=True)
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

# Thong tin lien he
class ContactModel(models.Model):
    pass