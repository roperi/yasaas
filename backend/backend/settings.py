"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env into the environment

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'localhost','127.0.0.1'
]

# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'corsheaders',
    'subscriptions.apps.SubscriptionsConfig',
    'auth_style',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'login_history',
    'easyaudit',

    # Backend
    'hero',
    'services',
    'products',
    'pricing',
    'about',
    'contact',
    'footer',
    
    # My Data Product
    'dataproduct',

]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "allauth.account.middleware.AccountMiddleware",
    "easyaudit.middleware.easyaudit.EasyAuditMiddleware",

]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],  # New
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

ADMIN_URL = "admin:index"


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'custom': {
            'format': '[%(levelname)s. %(name)s, (line #%(lineno)d) - %(asctime)s] %(message)s'
        },
    },
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        },
        'logfile': {
            'class':'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'log/backend.log'),
            'formatter': 'custom',
            'level': 'DEBUG',
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    "loggers": {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'subscriptions': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
        'emails': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
        },
    }
}

# # SECURITY-RELATED (TO BE USED IN PRODUCTION)
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# SECURE_HSTS_SECONDS = 31536000  # One year in seconds
# # Another security settings
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True
# SECURE_CONTENT_TYPE_NOSNIFF = True

# CORS
CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',
]

# CUSTOM TITLES AND HEADERS
INDEX_TITLE = "Data Dynamo"
SITE_TITLE = "API Portal"
SITE_HEADER = "Data Dynamo API"

# STRIPE
STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')
STRIPE_ENDPOINT_SECRET = os.environ.get('STRIPE_ENDPOINT_SECRET')
STRIPE_CUSTOMER_PORTAL_LINK = os.environ.get('STRIPE_CUSTOMER_PORTAL_LINK')

# DJANGO-ALLAUTH
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = 'http://localhost:3000/'
ACCOUNT_SIGNUP_REDIRECT_URL = '/redirect/'
LOGIN_REDIRECT_URL = "admin:index"
ACCOUNT_EMAIL_REQUIRED = True
# CUSTOM REDIRECT
CUSTOM_SIGNUP_REDIRECT_URL = 'http://localhost:3000/pricing-table/?user_id='

# EMAIL
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"  # Use this for development
# EMAIL_BACKEND = 'django_ses.SESBackend'  # Use this for staging/production
AWS_SES_ACCESS_KEY_ID = os.environ.get('AWS_SES_ACCESS_KEY_ID')
AWS_SES_SECRET_ACCESS_KEY = os.environ.get('AWS_SES_SECRET_ACCESS_KEY')
AWS_REGION_NAME = os.environ.get('AWS_REGION_NAME')

# JAZZMIN
JAZZMIN_SETTINGS = {
    # Logo to use for your site, must be present in static files, used for brand on top left
    "site_logo": "img/logo.svg",
    "copyright": "Data Dynamo",
}

# EASY AUDIT
DJANGO_EASY_AUDIT_UNREGISTERED_URLS_DEFAULT = [
    r'^/static/',
    r'^/favicon.ico$',
    r'^/webhook/',
]

DJANGO_EASY_AUDIT_UNREGISTERED_URLS_EXTRA = [
    r'^/admin/easyaudit/',
    r'^/admin/jsi18n/',
    r'^/admin/login/',
]

DJANGO_EASY_AUDIT_REGISTERED_URLS = [
    r'^/admin/',
]

# Track remote ID
DJANGO_EASY_AUDIT_REMOTE_ADDR_HEADER='HTTP_X_FORWARDED_FOR'
