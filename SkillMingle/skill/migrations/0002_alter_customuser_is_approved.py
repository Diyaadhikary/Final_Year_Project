# Generated by Django 5.1.3 on 2024-11-27 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("skill", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="is_approved",
            field=models.BooleanField(default=False),
        ),
    ]
