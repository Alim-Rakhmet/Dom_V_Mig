# Generated by Django 4.2.7 on 2023-12-22 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_photo_order_alter_realestate_photos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestate',
            name='property_type',
            field=models.IntegerField(),
        ),
    ]
