# Generated by Django 4.2.13 on 2025-02-14 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("translations", "0006_alter_language_status"),
    ]

    operations = [
        migrations.CreateModel(
            name="JobRole",
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
                    "code",
                    models.CharField(
                        help_text="Enter the code to distinguish the job role.",
                        max_length=255,
                        unique=True,
                    ),
                ),
                (
                    "name",
                    models.ForeignKey(
                        help_text="Select the slug of the name of the job role.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="translations.slug",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Member",
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
                    "full_name",
                    models.CharField(
                        help_text="Enter the full name of the team member. In Latin Characters.",
                        max_length=255,
                    ),
                ),
                (
                    "profile_image",
                    models.ImageField(
                        help_text="Upload the profile image of the team member.",
                        null=True,
                        upload_to="team_members/images/",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Enter a brief description of the team member.",
                        max_length=500,
                        null=True,
                    ),
                ),
                (
                    "job_role",
                    models.ForeignKey(
                        help_text="Select the job role of the team member.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="team_members.jobrole",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
