# Generated by Django 4.1.7 on 2024-12-20 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0041_photo_author_name_photo_author_photo_uri_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='apicalls',
            table='trip_api_calls',
        ),
    ]
