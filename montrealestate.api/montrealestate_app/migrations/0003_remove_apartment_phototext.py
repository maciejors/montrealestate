# Generated by Django 4.1.5 on 2023-01-09 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('montrealestate_app', '0002_apartment_constructionyear_apartment_isnew_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='photoText',
        ),
    ]