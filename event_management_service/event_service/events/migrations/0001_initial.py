# Generated by Django 5.1.1 on 2024-10-11 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Event",
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
                ("date", models.DateTimeField()),
                ("venue", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("event_type", models.CharField(max_length=255)),
                ("source", models.URLField()),
                ("comments", models.TextField(blank=True, null=True)),
                (
                    "added_by",
                    models.CharField(
                        choices=[("scraper", "Scraper Service"), ("user", "User")],
                        max_length=50,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "constraints": [
                    models.UniqueConstraint(
                        fields=("title", "date", "source"),
                        name="unique_event_constraint",
                    )
                ],
            },
        ),
    ]
