from pathlib import Path
from datetime import timedelta
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&-_xowo$@blkdzp4jvkvq--l9k2yq1x_rrrn8u)t%cm4&$h95^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True 

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # my apps/components
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    "rest_framework_simplejwt.token_blacklist",
    'corsheaders',
    
    # apps
    'myapp',
    'products',
    'crispy_forms',
    
    'oauth2_provider',
    'phone_field',
    'django_filters',
    
    'ckeditor',
    
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
AUTH_USER_MODEL ='products.User'

LOGIN_URL = 'signin'


REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        #  'rest_framework.permissions.AllowAny', # for all 
         'rest_framework.permissions.IsAuthenticated', # for authendicated user
        #  'rest_framework.permissions.IsAdminUser', # for is_staff =True
        #  'rest_framework.permissions.IsAuthenticatedOrReadOnly' # This class is useful when we need to set read permissions for anonymous users and read/write permissions for authenticated users. 
        #  'rest_framework.permissions.DjangoModelPermissions' # authendicated and has permission for post,put,delete operations
        #  'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly' #DjangoModelPermissionsOrAnonReadOnly permission class is the same as that of the DjangoModelPermissions class except it allows unauthenticated users to have read-only access to the API. 
        #  'rest_framework.permissions.DjangoObjectPermissions'
        # '''
        # The DjangoObjectPermissions allows per-object permissions on models, which can set permissions for individual rows in a table (model instances).The user must be authenticated to grant authorization and should be assigned with relevant per-object permissions and relevant model permissions. To set relevant per-object permissions, we need to subclass the DjangoObjectPermissions and implement the has_object_permission() method. 
        # '''
    ],
    
    'DEFAULT_AUTHENTICATION_CLASSES': [

        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        
        
    ],
}



SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=55),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=90),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': False,

    'ALGORITHM': 'HS256',
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('JWT',),
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:3000",
# ]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = (
    'GET','POST','PUT','DELETE','PATCH','OPTIONS'
)


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    'oauth2_provider.backends.OAuth2Backend',
)

SITE_ID = 2

LOGIN_REDIRECT_URL = '/'

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        # For each OAuth based provider, either add a ``SocialApp``
        # (``socialaccount`` app) containing the required client
        # credentials, or list them here:
        'APP': {
            'client_id': '1045824655965-bvcoqigok9ov035oaaditpp0gs7rmmp3.apps.googleusercontent.com',
            'secret': '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',
            'key': ''
        },
        
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        }
    }
}

OAUTH2_PROVIDER = {
    # this is the list of available scopes
    'SCOPES': {'read': 'Read scope', 'write': 'Write scope', 'groups': 'Access to your groups'}
}

OAUTH_ACCESS_TOKEN_MODEL = 'oauth2_provider.models.AccessToken'

MIDDLEWARE = [    
    'django.middleware.security.SecurityMiddleware',
    
    'corsheaders.middleware.CorsMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
  
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
]


ROOT_URLCONF = 'src.urls'

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

WSGI_APPLICATION = 'src.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myproducts',
        'USER': 'root',
        'PASSWORD': 'EllaiDhurai007',
        'HOST':'localhost',
        'PORT':'3306',
           'OPTIONS': {  
           'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",

      }     
    },
    # 'new_db' :{
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'newdb',
    #     'USER': 'root',
    #     'PASSWORD': 'EllaiDhurai007',
    #     'HOST':'localhost',
    #     'PORT':'3306',
    #        'OPTIONS': {  
    #        'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
    #     }
    # }
}

# DATABASE_ROUTERS = ['routers.db_routers.AuthRouter','routers.db_routers.new_db',] 

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
    
    # {
    #     'NAME': 'django_password_validators.password_character_requirements.password_validation'
    #             '.PasswordCharacterValidator',
    #     'OPTIONS': {
    #         'min_length_digit': 1,
    #         'min_length_alpha': 2,
    #         'min_length_special': 1,
    #         'min_length_lower': 4,
    #         'min_length_upper': 1,
    #         'special_characters': "~!@#$%^&*()_+{}\":;'[]"
    #     }
    # },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    # 'products.hashers.LegacyPasswordHasher'
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata' # default UTC is showing 5:30 hrs slow

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# static files are saved here
STATIC_ROOT = os.path.join(BASE_DIR,'')


# media files are stored here
MEDIA_URL = '/images/'
MEDIA_ROOT = os.path.join(BASE_DIR,'static/images')


# DJOSER = {
#     'LOGIN_FIELD' : 'email',
#     'USER_CREATE_PASSWORD_RETYPE':True,
#     'USERNAME_CHANGED_EMAIL_CONFIRMATION':True,
#     'PASSWORD_CHANGED_EMAIL_CONFIRMATION':True,
#     'SEND_CONFIRMATION_EMAIL':True,
#     'SET_USERNAME_RETYPE': True,
#     'SET_PASSWORD_RETYPE': True,
#     'PASSWORD_RESET_CONFIRM_URL':'password/reset/confirm/{uid}/{token}',
#     'USERNAME_RESET_CONFIRM_URL':'email/reset/confirm/{uid}/{token}',
#     'ACTIVATION_URL':"activate//{uid}/{token}",
#     'SEND_ACTIVATION_EMAIL':True
# }


# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# email link setup
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'ellaidhurai.97@gmail.com'
EMAIL_HOST_PASSWORD = 'svnqjmanicqisrzc'
EMAIL_USE_TLS = True



if DEBUG:
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)
    
    
    