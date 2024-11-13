# Generated by Django 4.1.7 on 2024-11-13 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0027_city_lat_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='city', to='trip.city'),
        ),
    ]
