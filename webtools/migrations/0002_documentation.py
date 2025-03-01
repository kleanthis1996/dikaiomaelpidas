# Generated by Django 4.2.13 on 2025-03-01 14:31

from django.db import migrations, models
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ("webtools", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Documentation",
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
                ("title", models.CharField(max_length=255)),
                (
                    "content",
                    django_ckeditor_5.fields.CKEditor5Field(verbose_name="Content"),
                ),
            ],
        ),
    ]
