# Generated by Django 5.1.4 on 2025-01-09 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Match",
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
                ("date", models.DateField(blank=True, null=True)),
                ("home_team", models.CharField(max_length=200)),
                ("away_team", models.CharField(max_length=200)),
                ("competition", models.CharField(max_length=200)),
                ("goals_for", models.PositiveIntegerField(default=0)),
                ("goals_against", models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Player",
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
                ("name", models.CharField(max_length=200)),
                ("birth_date", models.DateField(blank=True, null=True)),
                (
                    "position",
                    models.CharField(
                        choices=[
                            ("GK", "Goalkeeper"),
                            ("LB", "Left Back"),
                            ("RB", "Right Back"),
                            ("LWB", "Left Wing Back"),
                            ("RWB", "Right Wing Back"),
                            ("CB", "Center Back"),
                            ("CDM", "Central Defensive Midfielder"),
                            ("CM", "Central Midfielder"),
                            ("CAM", "Central Attacking Midfielder"),
                            ("LW", "Left Winger"),
                            ("RW", "Right Winger"),
                            ("ST", "Striker"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "pref_foot",
                    models.CharField(
                        choices=[("R", "Right"), ("L", "Left")], max_length=10
                    ),
                ),
                ("nationality", models.CharField(default="Unknown", max_length=200)),
                ("team", models.CharField(default="Free Agent", max_length=200)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")],
                        default="M",
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Performance",
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
                ("minutes", models.PositiveIntegerField(default=0)),
                ("goals", models.PositiveIntegerField(default=0)),
                ("assists", models.PositiveIntegerField(default=0)),
                ("shots", models.PositiveIntegerField(default=0)),
                ("shots_on_goals", models.PositiveIntegerField(default=0)),
                ("total_passes", models.PositiveIntegerField(default=0)),
                ("passes_completed", models.PositiveIntegerField(default=0)),
                ("xg", models.FloatField(default=0.0)),
                ("yellow_cards", models.PositiveIntegerField(default=0)),
                ("red_cards", models.PositiveIntegerField(default=0)),
                (
                    "match",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="football_app.match",
                    ),
                ),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="football_app.player",
                    ),
                ),
            ],
        ),
    ]
