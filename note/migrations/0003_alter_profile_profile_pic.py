# Generated by Django 4.2.3 on 2024-09-26 12:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("note", "0002_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_pic",
            field=models.ImageField(
                default="Default.png", upload_to="", verbose_name="image"
            ),
        ),
    ]
