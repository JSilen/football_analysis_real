# Generated by Django 5.1.4 on 2025-01-09 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("football_app", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="player",
            name="birth_date",
        ),
        migrations.AddField(
            model_name="player",
            name="age",
            field=models.CharField(default="Insert age...", max_length=10),
        ),
    ]
