# Generated by Django 5.0.4 on 2024-05-26 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comp',
            name='theme',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='randommatching',
            name='isMatched',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='randommatching',
            name='person',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='randommatching',
            name='priority',
            field=models.IntegerField(default=100, null=True),
        ),
        migrations.AddField(
            model_name='randommatching',
            name='recruitNum',
            field=models.IntegerField(default=0),
        ),
    ]
