# Generated by Django 4.1.5 on 2023-01-13 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('montrealestate_app', '0006_remove_apartment_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='commercial',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='detached',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='duplex',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='house',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='loftStudio',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='multiplex',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='other',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='quadruplex',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='triplex',
        ),
    ]
