# django
from django.db import models
# local
from translations.functions import get_english_text
from translations.models import Slug, Translation
from webtools.models import StatusAbstract


class JobRole(models.Model):
    name = models.ForeignKey(
        Slug,
        on_delete=models.CASCADE,
        help_text="Select the slug of the name of the job role.",
    )

    def __str__(self):
       return get_english_text(self.name)


class MemberCategory(models.Model):
    name = models.ForeignKey(
        Slug,
        on_delete=models.CASCADE,
        help_text="Select the slug of the name of the member category.",
    )

    code =models.CharField(
        max_length=255,
    )

    class Meta:
        verbose_name_plural = "Member Categories"

    def __str__(self):
        return get_english_text(self.name)


class Member(StatusAbstract):
    job_role = models.ForeignKey(
        JobRole,
        on_delete=models.CASCADE,
        help_text="Select the job role of the team member.",
    )

    category = models.ForeignKey(
        MemberCategory,
        on_delete=models.CASCADE,
        help_text="Select the category of the team member.",
    )

    full_name = models.CharField(
        max_length=255,
        help_text="Enter the full name of the team member. In Latin Characters.",
    )

    profile_image = models.ImageField(
        upload_to="images/team_members/",
        null=True,
        help_text="Upload the profile image of the team member.",
    )

    description = models.ForeignKey(
        Slug,
        null=True,
        on_delete=models.CASCADE,
        help_text="Select the slug of team member description.",
    )

    def __str__(self):
        return f"{self.full_name} - {get_english_text(self.job_role.name)}"
