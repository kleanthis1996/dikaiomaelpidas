# Generated by Django 4.2.13 on 2025-02-18 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("team_members", "0002_remove_jobrole_code_alter_member_job_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="job_role",
            field=models.ForeignKey(
                default="",
                help_text="Select the job role of the team member.",
                on_delete=django.db.models.deletion.CASCADE,
                to="team_members.jobrole",
            ),
            preserve_default=False,
        ),
    ]
