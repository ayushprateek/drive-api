# Generated by Django 3.2 on 2023-09-21 12:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='city_image', to='user.media'),
        ),
        migrations.CreateModel(
            name='WeirdAndWacky',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('description', models.CharField(blank=True, max_length=1100, null=True)),
                ('meta_data', models.JSONField(null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weirdandwacky_city', to='trip.city')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='weirdandwacky_banner', to='user.media')),
            ],
            options={
                'verbose_name': 'Attraction',
                'verbose_name_plural': 'Attractions',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('description', models.CharField(blank=True, max_length=1100, null=True)),
                ('meta_data', models.JSONField(null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='park_city', to='trip.city')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='park_banner', to='user.media')),
            ],
            options={
                'verbose_name': 'Park',
                'verbose_name_plural': 'Parks',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('description', models.CharField(blank=True, max_length=1100, null=True)),
                ('meta_data', models.JSONField(null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_city', to='trip.city')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food_banner', to='user.media')),
            ],
            options={
                'verbose_name': 'Food',
                'verbose_name_plural': 'Foods',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='FamilyFun',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('description', models.CharField(blank=True, max_length=1100, null=True)),
                ('meta_data', models.JSONField(null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familyfun_city', to='trip.city')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fun_banner', to='user.media')),
            ],
            options={
                'verbose_name': 'FamilyFun',
                'verbose_name_plural': 'FamilyFuns',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('description', models.CharField(blank=True, max_length=1100, null=True)),
                ('meta_data', models.JSONField(null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camp_city', to='trip.city')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='camp_banner', to='user.media')),
            ],
            options={
                'verbose_name': 'Attraction',
                'verbose_name_plural': 'Attractions',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('attraction', models.CharField(blank=True, choices=[('museums', 'Museums'), ('sightseeing', 'Sightseeing'), ('themeparks', 'Theme Parks'), ('zoosaquarium', 'Zoos & Aquarium'), ('others', 'Others')], max_length=200, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('description', models.CharField(blank=True, max_length=1100, null=True)),
                ('meta_data', models.JSONField(null=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attraction_city', to='trip.city')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attraction_banner', to='user.media')),
            ],
            options={
                'verbose_name': 'Attraction',
                'verbose_name_plural': 'Attractions',
                'ordering': ['-created_at'],
            },
        ),
    ]
