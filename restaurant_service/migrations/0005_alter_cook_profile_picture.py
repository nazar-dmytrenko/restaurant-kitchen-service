# Generated by Django 4.2.5 on 2024-01-19 15:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant_service", "0004_rename_cook_profile_picture_cook_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cook",
            name="profile_picture",
            field=models.ImageField(
                default="static/assets/img/def_pfp.png", upload_to="cooks"
            ),
        ),
    ]
