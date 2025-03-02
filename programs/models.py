# django
from django.db import models
# local
from translations.functions import get_english_text
from translations.models import Slug
from webtools.models import StatusAbstract


class Program(StatusAbstract):
    name = models.ForeignKey(
        Slug,
        related_name='program_name_slug',
        on_delete=models.CASCADE,
        help_text=f"Select the slug of the program name.",
    )

    description = models.ForeignKey(
        Slug,
        related_name='program_description_slug',
        on_delete=models.CASCADE,
        help_text=f"Select the slug of the program description.",
    )

    image = models.ImageField(
        upload_to="images/programs/",
        null=True,
        help_text="Upload the image of the program.",
    )

    def __str__(self):
        return f"{get_english_text(self.name)}"