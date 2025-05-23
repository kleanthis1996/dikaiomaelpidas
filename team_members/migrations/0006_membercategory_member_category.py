# Generated by Django 4.2.13 on 2025-03-18 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("translations", "0007_alter_language_code_alter_language_name_and_more"),
        ("team_members", "0005_alter_member_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="MemberCategory",
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
                ("code", models.CharField(max_length=255)),
                (
                    "name",
                    models.ForeignKey(
                        help_text="Select the slug of the name of the member category.",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="translations.slug",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="member",
            name="category",
            field=models.ForeignKey(
                default="",
                help_text="Select the category of the team member.",
                on_delete=django.db.models.deletion.CASCADE,
                to="team_members.membercategory",
            ),
            preserve_default=False,
        ),
    ]
