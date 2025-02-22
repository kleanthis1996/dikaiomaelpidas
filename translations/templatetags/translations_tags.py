# django
from django import template
# local
from translations.models import Slug, Translation

register = template.Library()


@register.simple_tag(takes_context=True, name="trans")
def translate(context, slug_code):
    """
    Given a slug code, get request language,
    retrieve the translation from the db and return the translated text
    :param slug_code:
    :param context:
    :return:
    """
    # Get language of user's request
    request = context.get("request")
    # Get all translations from request
    translations = getattr(request, "translations", {})
    # Get translation for requested slug and return it else return the slug code
    return translations.get(slug_code, slug_code)
