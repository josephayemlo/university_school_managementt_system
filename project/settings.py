# imports
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()



BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY') 

DEBUG = os.environ.get('DEBUG') == 'True'



ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    'daphne',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # other apps
    'django_countries',
    # installed apps
    'accounts.apps.AccountsConfig',
    'core.apps.CoreConfig',
    'managementportal.apps.ManagementportalConfig',
    'staffportal.apps.StaffportalConfig',
    'studentportal.apps.StudentportalConfig',
    'applications.apps.ApplicationsConfig',
    'studentchat.apps.StudentchatConfig',




    

]

AUTH_USER_MODEL = 'core.CustomUser'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    # Custom Middeware
    'core.middleware.ForceAspirantProfileCompletionMiddleware',
    'core.middleware.ForceAspirantToAspirantPortal',
    # Whitenoise
     "whitenoise.middleware.WhiteNoiseMiddleware",
]


ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],

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


WSGI_APPLICATION = 'project.wsgi.application'


# 🚀 Production: PostgreSQL on Railway
"""
import dj_database_url
DATABASES = {
    "default": dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}
"""
# 🧪 Development: SQLite locally or leave if you want to push your sqlite and use it
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = '/static/'  # best to add leading slash

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # <-- REQUIRED!

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login Redirect
LOGIN_REDIRECT_URL = '/accounts/'
LOGIN_URL = '/accounts/'

# 

CSRF_TRUSTED_ORIGINS = [
    'https://joseph-ayemlo-school-management.onrender.com'
]

# EmailBackend
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')




# Paystack
PAYSTACK_SECRET_KEY = os.environ.get('PAYSTACK_SECRET_KEY')
PAYSTACK_PUBLIC_KEY = os.environ.get('PAYSTACK_PUBLIC_KEY')
PAYSTACK_INITIALIZE_URL = os.environ.get('PAYSTACK_INITIALIZE_URL')
PAYSTACK_VERIFY_URL = os.environ.get('PAYSTACK_VERIFY_URL')
    

# Get Redis URL from environment or fallback to localhost (for local dev)
REDIS_URL = os.environ.get('REDIS_URL', 'redis://127.0.0.1:6379/0')


# Celery Configuaration | we are telling Celery to use Redis
CELERY_BROKER_URL = REDIS_URL
CELERY_ACCEPT_CONTENT = ['json'] #method of sending the task will be json
CELERY_TASK_SERIALIZER = 'json'



# ASGI setup
ASGI_APPLICATION = 'project.asgi.application'

# Django Channel layers Setup with Redis
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            'hosts': [REDIS_URL],  # Works for both dev and prod
        },
    },
}


