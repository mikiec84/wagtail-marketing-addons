import os

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('DATABASE_NAME', 'db.sqlite3'),
    }
}

ALLOWED_HOSTS = ['localhost']

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

SECRET_KEY = 'not needed'
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

ROOT_URLCONF = 'tests.urls'

STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

USE_TZ = False

TESTS_ROOT = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(TESTS_ROOT, 'site', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
            'debug': True,
        },
    },
]


MIDDLEWARE = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.core.middleware.SiteMiddleware',
)

INSTALLED_APPS = (
    'wagtail_marketing',

    'wagtail.contrib.modeladmin',
    'wagtail.search',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.images',
    'wagtail.documents',
    'wagtail.admin',
    'wagtail.core',

    'taggit',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'tests.site.pages',
)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',  # don't use the intentionally slow default password hasher
)

WAGTAIL_SITE_NAME = 'wagtail-marketing-addons test'