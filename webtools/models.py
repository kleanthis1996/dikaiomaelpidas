from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class StatusAbstract(models.Model):
    status = models.BooleanField(
        default=True,
        help_text="If checked, it will be visible on the website. If not it will hidden."
    )

    class Meta:
        abstract = True


class ContactInformation(models.Model):
    SOCIAL_CATEGORY = "social_category"
    CONTACT_CATEGORY = "contact_category"

    LOCATION = "location"
    PHONE = "phone"
    EMAIL = "email"
    FACEBOOK = "facebook"
    INSTAGRAM = "instagram"

    contact_information_categories = (
        (SOCIAL_CATEGORY, "Social Category"),
        (CONTACT_CATEGORY, "Contact Category"),
    )

    contact_value_type = (
        (LOCATION, "Location"),
        (PHONE, "Phone"),
        (EMAIL, "Email"),
        (FACEBOOK, "Facebook"),
        (INSTAGRAM, "Instagram"),
    )

    category = models.CharField(
        max_length=50,
        choices=contact_information_categories,
    )

    type = models.CharField(
        max_length=50,
        choices=contact_value_type,
    )

    value = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.type


class Documentation(models.Model):
    title = models.CharField(max_length=255)

    content = CKEditor5Field(
        "Content",
        config_name="default",
    )

    def __str__(self):
        return self.title


class Announcement(StatusAbstract):
    title = models.CharField(
        max_length=255,
        help_text="Title of the announcement. For internal use only."
    )

    image = models.ImageField(
        upload_to='images/announcements/',
        blank=True,
        null=True,
        help_text=f"Upload the image of the announcement."
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
