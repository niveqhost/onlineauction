from pathlib import Path
from decouple import config
from django.utils.translation import gettext_lazy as _
import os, sys

# MIME types warning on FireFox - Tat canh bao Js tren trinh duyet FireFox
import mimetypes
mimetypes.add_type("application/javascript", ".js", True)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', cast=bool, default=False)

# Cai dat de gui mail cho nguoi dung
TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

ALLOWED_HOSTS = [
    '127.0.0.1', 
    'localhost',
    # 'mysite@company.com.vn' <- Ten mien duoc su dung khi trien khai du an len internet
]

# Ghi de lop xac thuc nguoi dung
AUTH_USER_MODEL = 'authentication.CustomUser'

# Application definition
INSTALLED_APPS = [
    'jazzmin', # Giao dien trang quan tri
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication', # Xac thuc nguoi dung
    'auction', # Dau gia
    'modeltranslation',
    'django.contrib.admin',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # sau SessionMiddleware, truoc CommonMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Noi chua thu muc giao dien html
        'DIRS': [ os.path.join(BASE_DIR, 'templates') ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        # He quan tri co so du lieu MySQL
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USERNAME'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT')
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True # Tuy chinh dinh dang thoi gian theo gio dia phuong

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')   #python manage.py help, python manage py collectstatic
]

# Media url - Thu muc chua hinh anh, am thanh, da phuong tien
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Jazzmin settings - Cai dat giao dien trang quan tri
JAZZMIN_SETTINGS = {
    "language_chooser": True,
    "site_title": _("Online Auction Administration"),
    "site_brand": _("Auction Admin"),
}

# Email settings - Cau hinh phuong thuc gui email
EMAIL_USE_TLS = config('EMAIL_USE_TLS')
EMAIL_FROM_USER = config('EMAIL_FROM_USER')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')

# Language translation settings - Cai dat ho tro da ngon ngu
LANGUAGES = [
    ('vi', _('Vietnamese')),
    ('en', _('English'))
]
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]
LOCALE_DIRS = [
    os.path.join(BASE_DIR, 'locale')
]
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.i18n',
)
# Ho tro chuyen da ngon ngu trong co so du lieu 
MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'
MODELTRANSLATION_LANGUAGES = ('en', 'vi')
