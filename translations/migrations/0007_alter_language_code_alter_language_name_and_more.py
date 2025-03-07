# Generated by Django 4.2.13 on 2025-03-01 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("translations", "0006_alter_language_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="language",
            name="code",
            field=models.CharField(
                help_text="Enter a 2-digit ISO 639-1 language code.",
                max_length=2,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="language",
            name="name",
            field=models.CharField(
                help_text="Enter the name of the ISO 639-1 language code.",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="slug",
            name="code",
            field=models.CharField(
                help_text="Enter a code identifying the slug.",
                max_length=255,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="slug",
            name="description",
            field=models.CharField(
                blank=True, help_text="Enter a description of the slug.", max_length=255
            ),
        ),
        migrations.AlterField(
            model_name="translation",
            name="language",
            field=models.ForeignKey(
                help_text="Select the language of this translation",
                on_delete=django.db.models.deletion.CASCADE,
                to="translations.language",
            ),
        ),
        migrations.AlterField(
            model_name="translation",
            name="slug",
            field=models.ForeignKey(
                help_text="Select the slug identifying the translation.",
                on_delete=django.db.models.deletion.CASCADE,
                to="translations.slug",
            ),
        ),
        migrations.AlterField(
            model_name="translation",
            name="text",
            field=models.TextField(
                help_text="Enter the text of this translation", max_length=500
            ),
        ),
    ]
