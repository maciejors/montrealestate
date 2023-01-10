# Generated by Django 4.1.5 on 2023-01-09 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('district', models.CharField(max_length=255)),
                ('postalCode', models.CharField(max_length=255)),
                ('photoText', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('photoUrl', models.CharField(max_length=255)),
                ('googleMapAddressLink', models.CharField(max_length=255)),
                ('walkScoreMapped', models.CharField(max_length=255)),
                ('contactEmail', models.CharField(max_length=255)),
                ('contactPhoneNumber', models.CharField(max_length=255)),
            ],
        ),
    ]
