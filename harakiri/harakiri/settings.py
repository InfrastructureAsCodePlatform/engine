"""
Django settings for harakiri project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import datetime
from os import environ
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = environ["SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = environ["DEBUG"]

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    "django_json_widget",
    "rest_framework",
    "health_check",
    "health_check.db",
    "health_check.contrib.migrations",
    "encrypted_model_fields",
    "harakiri.core",
    "harakiri.users",
    "harakiri.boilerplates",
    "harakiri.modules",
    "harakiri.credentials",
    "harakiri.sources",
    "harakiri.projects",
    "harakiri.environments",
    "harakiri.blades",
    "harakiri.deployments",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "harakiri.urls"
AUTH_USER_MODEL = "users.User"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "harakiri.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": environ["DATABASE_NAME"],
        "USER": environ["DATABASE_USER"],
        "PASSWORD": environ["DATABASE_PASSWORD"],
        "HOST": environ["DATABASE_HOST"],
        "PORT": environ["DATABASE_PORT"],
        "CONN_MAX_AGE": 300,
        "TEST": {"NAME": environ["TEST_DATABASE_NAME"], "CHARSET": "utf8"},  # name to use for testrunner db
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(seconds=10800),  # 3 hours
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(seconds=86400),  # 1 day
    "AUTH_HEADER_TYPES": ("Bearer", "JWT"),
}

# rest framework
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ),
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ],
    "DEFAULT_FILTER_BACKENDS": ["rest_framework.filters.OrderingFilter"],
    "URL_FORMAT_OVERRIDE": "response_format",
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 10,
}

# redis / celery
REDIS_HOST = environ["REDIS_HOST"]
CELERY_DATE_FORMAT = "%Y-%m-%d %H:%M:%S %z"
CELERY_BROKER_URL = environ["CELERY_BROKER_URL"]
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_RESULT_SERIALIZER = "json"
CELERY_WORKER_ENABLE_REMOTE_CONTROL = False
CELERY_WORKER_SEND_TASK_EVENTS = False
CELERY_WORKER_CONCURRENCY = 1
CELERY_TASK_ACKS_LATE = True
CELERY_WORKER_PREFETCH_MULTIPLIER = 1
CELERY_TASK_DEFAULT_EXCHANGE_TYPE = "direct"
CELERY_TASK_DEFAULT_ROUTING_KEY = "celery"
CELERY_TASK_DEFAULT_EXCHANGE = "celery"
CELERY_TASK_DEFAULT_QUEUE = environ["CELERY_GENERAL_QUEUE"]
CELERY_TASK_QUEUES = {
    environ["CELERY_GENERAL_QUEUE"]: {"binding_key": "general.#"},
}
CELERY_TASK_ROUTES = {
    "harakiri.deployments.tasks.iac.IaC": {
        "queue": environ["CELERY_GENERAL_QUEUE"],
        "routing_key": "general.iac",
    },
    "harakiri.deployments.tasks.ci.CI": {
        "queue": environ["CELERY_GENERAL_QUEUE"],
        "routing_key": "general.ci",
    },
}
CELERY_IMPORTS = [
    "harakiri.deployments.tasks.iac",
    "harakiri.deployments.tasks.ci",
]

# admin
ADMIN_URL = f"{environ['API_SUBDOMAIN']}admin/"

FIELD_ENCRYPTION_KEY = environ["FIELD_ENCRYPTION_KEY"]
