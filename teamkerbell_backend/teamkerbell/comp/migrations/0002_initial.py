# Generated by Django 5.0.4 on 2024-05-18 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("comp", "0001_initial"),
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="randommatching",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="randommatchings",
                to="user.basicuser",
            ),
        ),
    ]
