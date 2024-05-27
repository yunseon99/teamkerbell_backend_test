# Generated by Django 5.0.4 on 2024-05-26 08:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0003_comp_theme_randommatching_ismatched_and_more'),
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviousWinning',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.TextField(null=True)),
                ('title', models.CharField(default='default_value', max_length=100)),
                ('interview', models.TextField()),
                ('comp', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='previouswinnings', to='comp.comp')),
            ],
        ),
    ]