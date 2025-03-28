# Generated by Django 4.2.13 on 2025-03-23 16:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("translations", "0007_alter_language_code_alter_language_name_and_more"),
        ("client_messages", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="VolunteerSector",
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
                ("code", models.CharField(max_length=50)),
                (
                    "name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="volunteer_sectors",
                        to="translations.slug",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VolunteerApplication",
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
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("date_of_birth", models.DateField()),
                ("home_address", models.CharField(max_length=255)),
                (
                    "phone_number",
                    models.CharField(
                        max_length=17,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                ("email", models.EmailField(max_length=255)),
                (
                    "experience_description",
                    models.TextField(blank=True, max_length=500),
                ),
                ("consent_given", models.BooleanField(default=False)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PE", "Pending"),
                            ("PR", "Processing"),
                            ("RE", "Rejected"),
                            ("CO", "Completed"),
                        ],
                        default="PE",
                        max_length=2,
                    ),
                ),
                ("date_submitted", models.DateField(auto_now_add=True)),
                (
                    "volunteer_sectors",
                    models.ManyToManyField(to="client_messages.volunteersector"),
                ),
            ],
        ),
    ]
