# Generated by Django 4.0.3 on 2022-03-29 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(blank=True, default='', max_length=25)),
                ('lastName', models.CharField(blank=True, default='', max_length=25)),
                ('initialDeposit', models.IntegerField(default='0')),
            ],
        ),
    ]
