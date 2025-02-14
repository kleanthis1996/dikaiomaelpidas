from django.db import models

from translations.models import Slug
from webtools.models import StatusAbstract


class JobRole(models.Model):
    code = models.CharField(
        max_length=255,
        unique=True,
        help_text="Enter the code to distinguish the job role."
    )

    name = models.ForeignKey(
        Slug,
        on_delete=models.CASCADE,
        help_text="Select the slug of the name of the job role.",
    )

    def __str__(self):
        return self.code


class Member(StatusAbstract):
    job_role = models.ForeignKey(
        JobRole,
        on_delete=models.CASCADE,
        help_text="Select the job role of the team member.",
    )

    full_name = models.CharField(
        max_length=255,
        help_text="Enter the full name of the team member. In Latin Characters.",
    )

    profile_image = models.ImageField(
        upload_to="team_members/images/",
        null=True,
        help_text="Upload the profile image of the team member.",
    )

    description = models.TextField(
        max_length=500,
        null=True,
        help_text="Enter a brief description of the team member.",
    )

    def __str__(self):
        return self.full_name
