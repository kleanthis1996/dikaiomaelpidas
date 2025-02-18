from translations.models import Translation


def get_english_text(slug):
    """
    Function used to get english text. To be used in various places in cms
    :param slug:
    :return:
    """
    english_text = Translation.objects.filter(slug=slug, language__code="en").first()
    return english_text.text if english_text else slug.code