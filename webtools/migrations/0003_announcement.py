# Generated by Django 4.2.13 on 2025-03-27 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webtools", "0002_documentation"),
    ]

    operations = [
        migrations.CreateModel(
            name="Announcement",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status",
                    models.BooleanField(
                        default=True,
                        help_text="If checked, it will be visible on the website. If not it will hidden.",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Title of the announcement. For internal use only.",
                        max_length=255,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Upload the image of the announcement.",
                        null=True,
                        upload_to="images/announcements/",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
