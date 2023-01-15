# Generated by Django 4.1.5 on 2023-01-12 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('montrealestate_app', '0004_alter_apartment_latitude_alter_apartment_longitude'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apartment',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='apartment',
            name='longitude',
        ),
        migrations.AddField(
            model_name='apartment',
            name='apartment',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='commercial',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='detached',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='duplex',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='house',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='loftStudio',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='multiplex',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='other',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='quadruplex',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='apartment',
            name='triplex',
            field=models.BooleanField(default=True),
        ),
    ]
