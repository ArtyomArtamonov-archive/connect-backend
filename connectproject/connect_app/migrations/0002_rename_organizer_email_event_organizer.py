# Generated by Django 3.2.2 on 2021-05-15 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='organizer_email',
            new_name='organizer',
        ),
    ]