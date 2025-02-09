from django.db import models


class Language(models.Model):
    code = models.CharField(
        max_length=2,
        unique=True,
        help_text="Please enter a 2-digit ISO 639-1 language code.",
    )

    name = models.CharField(
        max_length=255,
        help_text="Please enter the name of the ISO 639-1 language code.",
    )

    def __str__(self):
        return self.name


class Slug(models.Model):
    code = models.CharField(
        max_length=255,
        unique=True,
        help_text="Please enter a code identifying the slug.",
    )

    description = models.CharField(
        max_length=255,
        blank=True,
        help_text="Please enter a description of the slug.",
    )

    def __str__(self):
        return self.code


class Translation(models.Model):
    slug = models.ForeignKey(
        Slug,
        on_delete=models.CASCADE,
        help_text="Please select the slug identifying the translation."
    )

    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        help_text="Please select the language of this translation",
    )

    text = models.CharField(
        max_length=255,
        help_text="Please enter the text of this translation",
    )

    def __str__(self):
        return f"{self.slug.code}-{self.language.code}"
