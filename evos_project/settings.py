from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent



SECRET_KEY = 'django-insecure-+tr)#sz181cz8_8#%f+xpv9@=wkrwablvd@d^8p2=*_-k$s9&x'

DEBUG = True

ALLOWED_HOSTS = []



INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'app',
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

ROOT_URLCONF = 'evos_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'evos_project.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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



STATIC_URL = 'static/'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#
# JAZZMIN_SETTINGS = {
#     "site_title": "Dilmurod Admin",
#
#     "site_header": "EVOS",
#
#     "site_brand": "EVOS",
#
#     "site_logo": "books/img/logo.png",
#
#     "login_logo": None,
#
#     "login_logo_dark": None,
#
#     "site_logo_classes": "img-circle",
#
#     "site_icon": None,
#
#     "welcome_sign": "Welcome to the library",
#
#     "copyright": "Acme Library Ltd",
#
#     "search_model": ["auth.User", "auth.Group"],
#
#     "user_avatar": None,
#
#
#
#     "topmenu_links": [
#
#         {"name": "Home",  "url": "admin:index", "permissions": ["auth.view_user"]},
#
#         {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
#
#         {"model": "auth.User"},
#
#         {"app": "books"},
#     ],
#
#
#     "usermenu_links": [
#         {"name": "Support", "url": "https://github.com/farridav/django-jazzmin/issues", "new_window": True},
#         {"model": "auth.user"}
#     ],
#
#
#     "show_sidebar": True,
#
#     "navigation_expanded": True,
#
#     "hide_apps": [],
#
#     "hide_models": [],
#
#     "order_with_respect_to": ["auth", "books", "books.author", "books.book"],
#
#     "custom_links": {
#         "books": [{
#             "name": "Make Messages",
#             "url": "make_messages",
#             "icon": "fas fa-comments",
#             "permissions": ["books.view_book"]
#         }]
#     },
#
#     "icons": {
#         "auth": "fas fa-users-cog",
#         "auth.user": "fas fa-user",
#         "auth.Group": "fas fa-users",
#     },
#     "default_icon_parents": "fas fa-chevron-circle-right",
#     "default_icon_children": "fas fa-circle",
#
#
#     "related_modal_active": False,
#
#     "custom_css": None,
#     "custom_js": None,
#     "use_google_fonts_cdn": True,
#     "show_ui_builder": False,
#
#
#     "changeform_format": "horizontal_tabs",
#     "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs"},
#
#}
