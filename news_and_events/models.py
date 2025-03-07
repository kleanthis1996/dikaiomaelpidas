# local
import os
# django
from django.db import models
# local
from translations.models import Slug, Language, Translation
from webtools.models import StatusAbstract
from translations.functions import get_english_text
# third party
from django_ckeditor_5.fields import CKEditor5Field


class PostCategory(models.Model):
    code = models.CharField(
        max_length=255,
        unique=True,
        help_text=f"Enter the code to be used in the codebase."
    )

    name = models.ForeignKey(
        Slug,
        on_delete=models.CASCADE,
        help_text=f"Select the slug of the post category name."
    )

    class Meta:
        verbose_name_plural = 'Post Categories'

    def __str__(self):
        return get_english_text(self.name)


class Post(models.Model):
    category = models.ForeignKey(
        PostCategory,
        on_delete=models.RESTRICT,
        help_text=f"Choose the category of the post."
    )

    title = models.ForeignKey(
        Slug,
        on_delete=models.RESTRICT,
        help_text=f"Choose the slug of the post title."
    )

    image = models.ImageField(
        upload_to='images/posts/',
        blank=True,
        null=True,
        help_text=f"Upload the image of the post."
    )

    published_date = models.DateField()

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return get_english_text(self.title)


class PostVariation(StatusAbstract):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        help_text=f"Choose the main post this variation belongs to."
    )

    language = models.ForeignKey(
        Language,
        on_delete=models.CASCADE,
        help_text=f"Choose the language of this variation of the selected post."
    )

    content = CKEditor5Field(
        "Content",
        config_name="default"
    )

    def __str__(self):
        return f"{self.post} - {self.language}"
