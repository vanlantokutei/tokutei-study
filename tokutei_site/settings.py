"""
Django settings for tokutei_site project.
"""
import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-3hwlbfhyx(!ci^%&7!8)xku#!h8onxky&b20w*k89g)a1i2uua'
DEBUG = False
ALLOWED_HOSTS = ["onthitokutei.com", "www.onthitokutei.com", ".onrender.com", "127.0.0.1", "localhost"]
CSRF_TRUSTED_ORIGINS = ["https://onthitokutei.com", "https://www.onthitokutei.com"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'study',
    'notifications',
    'notifications_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware','whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'study.middleware.RemoveVocabularyFlagMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
ROOT_URLCONF = 'tokutei_site.urls'
TEMPLATES = [{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION = 'tokutei_site.wsgi.application'
DATABASES = {'default': dj_database_url.config(default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}", conn_max_age=600, conn_health_checks=True)}
AUTH_PASSWORD_VALIDATORS = [
    {'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
LANGUAGE_CODE='en-us'
TIME_ZONE='UTC'
USE_I18N=True
USE_TZ=True
STATIC_URL='/static/'
STATIC_ROOT=BASE_DIR / 'staticfiles'
STATICFILES_DIRS=[('focus_music', BASE_DIR / 'tokutei_focus_mix_7_mp3_96k')]
LOGIN_REDIRECT_URL='/'
LOGOUT_REDIRECT_URL='/'

EMAIL_BACKEND=os.getenv('EMAIL_BACKEND','tokutei_site.resend_backend.ResendEmailBackend')
EMAIL_HOST=os.getenv('EMAIL_HOST','smtp.gmail.com')
EMAIL_PORT=int(os.getenv('EMAIL_PORT','587'))
EMAIL_USE_TLS=os.getenv('EMAIL_USE_TLS','true').lower() == 'true'
EMAIL_HOST_USER=os.getenv('EMAIL_HOST_USER','')
EMAIL_HOST_PASSWORD=os.getenv('EMAIL_HOST_PASSWORD','')
DEFAULT_FROM_EMAIL=os.getenv('DEFAULT_FROM_EMAIL','Ôn Thi Tokutei <noreply@onthitokutei.com>')
ADMIN_NOTIFICATION_EMAIL=os.getenv('ADMIN_NOTIFICATION_EMAIL', EMAIL_HOST_USER)
EMAIL_TIMEOUT=int(os.getenv('EMAIL_TIMEOUT','20'))

RESEND_API_KEY=os.getenv('RESEND_API_KEY','')
RESEND_FROM_EMAIL=os.getenv('RESEND_FROM_EMAIL','Ôn Thi Tokutei <noreply@onthitokutei.com>')

PREMIUM_BANK_INFO=os.getenv('PREMIUM_BANK_INFO','Thông tin chuyển khoản sẽ được Admin cập nhật.')
