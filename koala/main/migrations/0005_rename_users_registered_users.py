# Generated by Django 4.0.1 on 2022-01-20 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_users_date_created_users_date_updated'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Registered_Users',
        ),
    ]
