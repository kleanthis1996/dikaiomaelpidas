# django
from django.db import models
# local
from translations.functions import get_english_text
from translations.models import Slug
from webtools.models import StatusAbstract


class ProgramCategory(models.Model):
    name = models.ForeignKey(
        Slug,
        on_delete=models.CASCADE,
        help_text="Select the slug of the program category.",
    )

    code = models.CharField(
        max_length=255,
    )

    class Meta:
        verbose_name_plural = "Program Categories"

    def __str__(self):
        return get_english_text(self.name)

class Program(StatusAbstract):
    category = models.ForeignKey(
        ProgramCategory,
        on_delete=models.CASCADE,
        help_text="Select the program category.",
    )

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