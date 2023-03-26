# Generated by Django 4.1.7 on 2023-03-08 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enter", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-umumiy_bali"]},
        ),
        migrations.AlterField(
            model_name="post",
            name="exam_day",
            field=models.CharField(
                choices=[
                    ("kunlik imtihon", "kunlik imtihon"),
                    ("haftalik imtihon", "haftalik imtihon"),
                    ("Oylik Imtihon", "Oylik Imtihon"),
                    ("Yillik Imtihon", "Yillik Imtihon"),
                ],
                default="Haftalik",
                max_length=22,
            ),
        ),
    ]
