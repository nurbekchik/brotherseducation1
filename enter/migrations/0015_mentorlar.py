# Generated by Django 4.1.7 on 2023-03-23 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enter", "0014_image_class"),
    ]

    operations = [
        migrations.CreateModel(
            name="Mentorlar",
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
                ("name", models.CharField(max_length=150)),
                ("fani", models.CharField(max_length=150)),
                ("izoh", models.CharField(max_length=200)),
                ("rasmi", models.ImageField(upload_to="images/")),
                ("telegram_linki", models.CharField(max_length=300)),
                ("telephone", models.CharField(max_length=30)),
            ],
        ),
    ]