# Generated by Django 3.0 on 2019-12-29 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pilot',
            name='bike_name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
