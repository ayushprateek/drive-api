# Generated by Django 4.1.7 on 2024-12-10 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0034_alter_site_place_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='ad_status',
            field=models.IntegerField(default=0),
        ),
    ]
