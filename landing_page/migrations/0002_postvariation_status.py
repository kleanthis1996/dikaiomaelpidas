# Generated by Django 4.2.13 on 2025-02-10 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("landing_page", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="postvariation",
            name="status",
            field=models.BooleanField(
                default=True,
                help_text="If checked, it will be visible on the website. If not it will hidden.",
            ),
        ),
    ]
