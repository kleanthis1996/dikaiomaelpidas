"""
Django settings for dikeomaelpidas project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

from django.templatetags.static import static
from django.urls import reverse_lazy
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = [
    # Django custom theme
    "unfold",
    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Local apss
    "landing_page",
    "translations",
    "webtools",
    "client_messages",
    "news_and_events",
    "team_members",
    "programs",
    # Third party apps
    "django_ckeditor_5",
    "ckeditor_uploader",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "translations.middleware.LanguageMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "dikeomaelpidas.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS":  [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "dikeomaelpidas.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "/staticfiles/"
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = "/mediafiles/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
UNFOLD = {
    "SITE_TITLE": "Dikaioma Elpidas",
    "SITE_HEADER": "Dikaioma Elpidas CMS",
    "STYLES": [lambda request: static("assets/css/ck_editor_fix.css")],
    "SITE_ICON": lambda request: static("assets/images/logo.webp"),
    "DASHBOARD_CALLBACK": "landing_page.views.dashboard_callback",
    "THEME": "light",
    "TABS": [
        {
            "page": "client_message",
            "models": ["client_messages.contactusmessage", "client_messages.volunteersector", "client_messages.volunteerapplication"],
            "items": [
                {
                    "title": "Contact us Messages",
                    "link": reverse_lazy("admin:client_messages_contactusmessage_changelist"),
                },
                {
                    "title": "Volunteer Sectors",
                    "link": reverse_lazy("admin:client_messages_volunteersector_changelist"),
                },
                {
                    "title": "Volunteer Applications",
                    "link": reverse_lazy("admin:client_messages_volunteerapplication_changelist"),
                }
            ]
        },
        {
            "page": "news_and_events",
            "models": ["news_and_events.post", "news_and_events.postcategory"],
            "items": [
                {
                    "title": "Posts",
                    "link": reverse_lazy("admin:news_and_events_post_changelist"),
                },
                {
                    "title": "Posts Categories",
                    "link": reverse_lazy("admin:news_and_events_postcategory_changelist"),
                },
            ],
        },
        {
            "page": "team_members",
            "models": ["team_members.member", "team_members.membercategory", "team_members.jobrole"],
            "items": [
                {
                    "title": "Team Members",
                    "link": reverse_lazy("admin:team_members_member_changelist"),
                },
                {
                    "title": "Team Members Categories",
                    "link": reverse_lazy("admin:team_members_membercategory_changelist"),
                },
                {
                    "title": "Job Roles",
                    "link": reverse_lazy("admin:team_members_jobrole_changelist"),
                }
            ]
        },
        {
            "page": "translations",
            "models": ["translations.language", "translations.slug", ],
            "items": [
                {
                    "title": "Slugs",
                    "link": reverse_lazy("admin:translations_slug_changelist"),
                },
                {
                    "title": "Languages",
                    "link": reverse_lazy("admin:translations_language_changelist"),
                },
            ]
        },
        {
            "page": "programs",
            "models": ["programs.program", "programs.programcategory"],
            "items": [
                {
                    "title": "Programs",
                    "link": reverse_lazy("admin:programs_program_changelist"),
                },
                {
                    "title": "Program Categories",
                    "link": reverse_lazy("admin:programs_programcategory_changelist"),
                }
            ]
        }
    ],
    "SIDEBAR": {
        "show_all_applications": True,
        "navigation": [
            {
                "title": "Navigation",
                "items": [
                    {
                        "title": "Client Messages",
                        "icon": "mail",
                        "badge": "client_messages.utils.client_messages_badge_callback",
                        "link": reverse_lazy("admin:client_messages_contactusmessage_changelist"),
                    },
                    {
                        "title": "Posts",
                        "icon": "article",
                        "link": reverse_lazy("admin:news_and_events_post_changelist"),
                    },
                    {
                        "title": "Team Members",
                        "icon": "groups",
                        "link": reverse_lazy("admin:team_members_member_changelist"),
                    },
                    {
                        "title": "Translations",
                        "icon": "language",
                        "link": reverse_lazy("admin:translations_slug_changelist"),
                    },
                    {
                        "title": "Programs",
                        "icon": "book",
                        "link": reverse_lazy("admin:programs_program_changelist"),
                    },
                    {
                        "title": "Contact Information",
                        "icon": "phone",
                        "link": reverse_lazy("admin:webtools_contactinformation_changelist"),
                    },
                    {
                        "title": "Announcements",
                        "icon": "campaign",
                        "link": reverse_lazy("admin:webtools_announcement_changelist"),
                    },
                    {
                        "title": "Documentation",
                        "icon": "description",
                        "link": reverse_lazy("admin:webtools_documentation_changelist"),
                    }
                ],
            },
            {
                "title": "Users & Groups",
                "collapsible": True,
                "items": [
                    {
                        "title": "Users",
                        "icon": "person",
                        "link": reverse_lazy("admin:auth_user_changelist"),
                    },
                    {
                        "title": "Groups",
                        "icon": "group",
                        "link": reverse_lazy("admin:auth_group_changelist"),
                    },
                ],
            },
        ],
    },
}

CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "underline",
            "link",
            "blockQuote",
            "codeBlock",
            "imageUpload",
            "bulletedList",
            "numberedList",
            "horizontalLine",
            "insertTable",
            "mediaEmbed",
            "undo",
            "redo",
        ],
        "upload_url": "/ckeditor5/image_upload/",
    }
}
