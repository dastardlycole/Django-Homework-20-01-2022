# Generated by Django 4.0.1 on 2022-01-19 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='viewing_price',
            field=models.FloatField(null=True),
        ),
    ]
