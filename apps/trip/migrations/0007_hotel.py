# Generated by Django 3.2 on 2023-10-03 11:36

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0006_auto_20230929_0626'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.TextField()),
                ('description', models.TextField(null=True)),
                ('contact_info', models.JSONField(default=dict)),
                ('check_in_data', models.JSONField(default=dict)),
                ('address', models.JSONField(default=dict)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('hotel_reviews', models.JSONField(default=dict)),
                ('amenities', models.JSONField(default=dict)),
                ('service_amenities', models.JSONField(default=dict)),
                ('facility_overview', models.TextField(blank=True, null=True)),
                ('hotel_policy', models.JSONField(default=dict)),
                ('meta_data', models.JSONField(default=dict)),
                ('cover_image', models.TextField(null=True)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(null=True), default=list, size=None)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hotels_city', to='trip.city')),
            ],
            options={
                'verbose_name': 'Hotel',
                'verbose_name_plural': 'Hotels',
                'ordering': ['-created_at'],
            },
        ),
    ]
