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
    # Get language of user's request
    request = context.get("request")
    lang = getattr(request, "language", "en")

    # Fetch the translation in one query, avoiding multiple lookups
    translation = (
        Translation.objects
        .select_related("slug", "language")
        .filter(slug__code=slug_code, language__code=lang)
        .first()
    )

    return translation.text if translation else slug_code
