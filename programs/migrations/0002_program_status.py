# Generated by Django 4.2.13 on 2025-02-21 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programs", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="program",
            name="status",
            field=models.BooleanField(
                default=True,
                help_text="If checked, it will be visible on the website. If not it will hidden.",
            ),
        ),
    ]
