# Generated by Django 4.2.5 on 2025-02-13 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("title", models.CharField(max_length=20)),
                ("description", models.TextField()),
                ("customer_review_rank", models.IntegerField()),
                ("author", models.CharField(max_length=15)),
                ("author_info", models.TextField()),
                ("author_works", models.CharField(max_length=50)),
                ("cover_image", models.ImageField(blank=True, upload_to="")),
                (
                    "audio_file",
                    models.FileField(blank=True, null=True, upload_to="tts/"),
                ),
            ],
        ),
    ]
