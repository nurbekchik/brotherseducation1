# Generated by Django 4.1.7 on 2023-03-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enter", "0015_mentorlar"),
    ]

    operations = [
        migrations.CreateModel(
            name="Feedbacks",
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
                ("surname", models.CharField(max_length=150)),
                ("phone_number", models.CharField(max_length=30)),
                ("message", models.CharField(max_length=350)),
            ],
        ),
    ]
