from django.db import models


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