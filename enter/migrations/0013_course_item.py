# Generated by Django 4.1.7 on 2023-03-23 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enter", "0012_rename_courses_course_data"),
    ]

    operations = [
        migrations.CreateModel(
            name="Course_item",
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
                ("cost", models.IntegerField(default=200000)),
                ("good", models.CharField(max_length=150)),
                ("good1", models.CharField(max_length=150)),
                ("good2", models.CharField(max_length=150)),
                ("good3", models.CharField(max_length=150)),
                ("good4", models.CharField(max_length=150)),
            ],
        ),
    ]
