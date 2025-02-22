# system
from functools import wraps
# local
from translations.models import Translation


def get_translations_information(view_func):
    """
    Decorator used to load translations information in all HTML rendering views
    :param view_func:
    :return:
    """
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        # Get all translations based on the language in request
        current_language_translations = Translation.objects.select_related("slug", "language").filter(
            language__code=request.language)
        # Parse the dict containing slug code as key and translation as value
        result = {}
        for translation in current_language_translations:
            result[translation.slug.code] = translation.text
        # Add it in request
        request.translations = result
        return view_func(request, *args, **kwargs)
    return wrapped_view