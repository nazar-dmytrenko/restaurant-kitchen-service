# Generated by Django 4.2.5 on 2024-01-19 18:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant_service", "0007_alter_cook_profile_picture_alter_dish_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cook",
            name="profile_picture",
            field=models.ImageField(
                blank=True, default="picture/def_pfp.png", upload_to="avatars"
            ),
        ),
        migrations.AlterField(
            model_name="dish",
            name="picture",
            field=models.ImageField(default="picture/def_pfp.png", upload_to="dish"),
        ),
    ]
