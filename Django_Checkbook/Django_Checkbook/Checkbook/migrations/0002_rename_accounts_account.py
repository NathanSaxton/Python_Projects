# Generated by Django 4.0.3 on 2022-03-29 22:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Checkbook', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Accounts',
            new_name='Account',
        ),
    ]
