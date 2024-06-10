# Generated by Django 3.2 on 2023-11-06 05:27

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20230925_0827'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPlanTripLogs',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('route_request_timestamp', models.DateTimeField()),
                ('origin', models.TextField()),
                ('destination', models.TextField()),
                ('travel_time', models.CharField(max_length=10)),
                ('categories', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), blank=True, null=True, size=None)),
                ('discount_type', models.CharField(blank=True, max_length=256, null=True)),
                ('meta_data', models.JSONField(default=dict)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
