# Generated by Django 4.1.7 on 2023-03-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enter", "0013_course_item"),
    ]

    operations = [
        migrations.CreateModel(
            name="Image_class",
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
                ("img", models.ImageField(upload_to="images/")),
            ],
        ),
    ]