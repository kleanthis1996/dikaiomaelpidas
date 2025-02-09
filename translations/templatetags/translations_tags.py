from django import template

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
    try:
        request = context["request"]
        lang = getattr(request, "language", "en")
        # Get slug
        slug = Slug.objects.get(code=slug_code)
        # Get translation for requested language
        translation = slug.translations.get(language__code=lang)
        return translation.text
    except ValueError as e:
        print(f"Translation for {slug_code} not found")
        return slug_code
