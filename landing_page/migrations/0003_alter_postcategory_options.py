# Generated by Django 4.2.13 on 2025-02-10 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("landing_page", "0002_postvariation_status"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="postcategory",
            options={"verbose_name_plural": "Post Categories"},
        ),
    ]
