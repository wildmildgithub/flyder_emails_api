from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR            = Path(__file__).resolve().parent.parent
SECRET_KEY          = os.environ.get('DJANGO_SECRET_KEY', 'z*l$(*b@&jkx*56h(uz1s2c%nh2ckw)o(2c$k)!l)(sywc5$s0')

ROOT_URLCONF        = 'backend.urls'
WSGI_APPLICATION    = 'backend.wsgi.application'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'core.apps.CoreConfig',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# Internationalization
LANGUAGE_CODE           = 'en-us'
TIME_ZONE               = 'UTC'
USE_I18N                = True
USE_L10N                = True
USE_TZ                  = True

# Static files (CSS, JavaScript, Images)
STATIC_URL              = '/static/'
STATICFILES_DIRS        = [os.path.join(BASE_DIR, 'static_in_env')]
STATIC_ROOT             = os.path.join(BASE_DIR, 'static_root')

# Gmail SMTP 
# EMAIL_BACKEND         = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST            = 'smtp.gmail.com'
# EMAIL_HOST_USER       = '*@gmail.com'
# EMAIL_HOST_PASSWORD   = 'ipumspnmqbcnkmgl' #past the key or password app here
# EMAIL_PORT            = 587
# EMAIL_USE_TLS         = True
# DEFAULT_FROM_EMAIL    = 'default from email'
