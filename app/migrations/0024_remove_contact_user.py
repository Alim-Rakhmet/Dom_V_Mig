# Generated by Django 4.2.7 on 2023-12-25 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
    ]
