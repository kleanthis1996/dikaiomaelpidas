from django.db import models

class StatusAbstract(models.Model):
    status = models.BooleanField(
        default=True,
        help_text="If checked, it will be visible on the website. If not it will hidden."
    )

    class Meta:
        abstract = True