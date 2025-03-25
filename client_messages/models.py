# django
from django.core.validators import RegexValidator
from django.db import models

# local
from translations.models import Slug

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
)


class ContactUsMessage(models.Model):
    STATUS_PENDING = "PE"
    STATUS_PROCESSING = "PR"
    STATUS_REJECTED = "RE"
    STATUS_COMPLETED = "CO"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_PROCESSING, "Processing"),
        (STATUS_REJECTED, "Rejected"),
        (STATUS_COMPLETED, "Completed"),
    ]

    first_name = models.CharField(
        max_length=255
    )

    last_name = models.CharField(
        max_length=255
    )

    email = models.EmailField(
        max_length=255
    )

    message = models.TextField(
        max_length=500,
    )

    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )

    date_submitted = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return f'Message:{self.first_name} {self.last_name} {self.date_submitted}'


class VolunteerSector(models.Model):
    code = models.CharField(
        max_length=50,
        blank=True,
    )

    name = models.ForeignKey(
        Slug,
        on_delete=models.CASCADE,
        related_name='volunteer_sectors',
    )

    is_other = models.BooleanField(
        default=False,
    )

class VolunteerApplication(models.Model):
    STATUS_PENDING = "PE"
    STATUS_PROCESSING = "PR"
    STATUS_REJECTED = "RE"
    STATUS_COMPLETED = "CO"

    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_PROCESSING, "Processing"),
        (STATUS_REJECTED, "Rejected"),
        (STATUS_COMPLETED, "Completed"),
    ]

    first_name = models.CharField(
        max_length=255
    )

    last_name = models.CharField(
        max_length=255
    )

    date_of_birth = models.DateField()

    home_address = models.CharField(
        max_length=255
    )

    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
    )

    email = models.EmailField(
        max_length=255
    )

    volunteer_sectors = models.ManyToManyField(
        VolunteerSector,
    )

    experience_description = models.TextField(
        max_length=500,
        blank=True,
    )

    consent_given = models.BooleanField(
        default=False,
    )

    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=STATUS_PENDING,
    )

    date_submitted = models.DateField(
        auto_now_add=True
    )

    def __str__(self):
        return f'Volunteer Application: {self.first_name} {self.last_name} {self.date_submitted}'