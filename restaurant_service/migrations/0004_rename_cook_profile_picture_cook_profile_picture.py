# Generated by Django 4.2.5 on 2024-01-19 15:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("restaurant_service", "0003_alter_dish_picture"),
    ]

    operations = [
        migrations.RenameField(
            model_name="cook",
            old_name="cook_profile_picture",
            new_name="profile_picture",
        ),
    ]
