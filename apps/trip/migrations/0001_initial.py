# Generated by Django 4.1.7 on 2024-06-24 07:08

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attraction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('attraction', models.CharField(blank=True, choices=[('museums', 'Museums'), ('sightseeing', 'Sightseeing'), ('themeparks', 'Theme Parks'), ('zoosaquarium', 'Zoos & Aquarium'), ('others', 'Others')], max_length=200, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(null=True), default=list, size=None)),
                ('meta_data', models.JSONField(default=dict)),
            ],
            options={
                'verbose_name': 'Attraction',
                'verbose_name_plural': 'Attractions',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=100)),
                ('icon_url', models.URLField(blank=True, max_length=255, null=True)),
                ('image_url', models.URLField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(null=True), default=list, size=None)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'City',
                'verbose_name_plural': 'Cities',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('type', models.CharField(blank=True, choices=[('music', 'Music'), ('festivals', 'Festivals'), ('sports', 'Sports'), ('holidays', 'Holidays'), ('others', 'Others')], max_length=200, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(null=True), default=list, size=None)),
                ('meta_data', models.JSONField(default=dict)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_city', to='trip.city')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ExtremeSport',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=500, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('description', models.TextField(null=True)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(null=True), default=list, size=None)),
                ('meta_data', models.JSONField(default=dict)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extremesport_city', to='trip.city')),
            ],
            options={
                'verbose_name': 'Extreme Sport',
                'verbose_name_plural': 'Extreme Sports',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Geometry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalSite',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=500, null=True)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('description', models.TextField(null=True)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(null=True), default=list, size=None)),
                ('meta_data', models.JSONField(default=dict)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historicalsite_city', to='trip.city')),
            ],
            options={
                'verbose_name': 'Historical Site',
                'verbose_name_plural': 'Historical Sites',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('place_id', models.CharField(default='', max_length=500, unique=True)),
                ('name', models.TextField()),
                ('description', models.TextField(null=True)),
                ('contact_info', models.JSONField(default=dict)),
                ('check_in_data', models.JSONField(default=dict)),
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
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('rating', models.FloatField(default=0, null=True)),
                ('user_ratings_total', models.IntegerField(default=0, null=True)),
                ('start_price', models.FloatField(null=True)),
                ('end_price', models.FloatField(null=True)),
                ('icon', models.CharField(blank=True, max_length=500, null=True)),
                ('discount_url', models.CharField(max_length=400, null=True)),
                ('business_status', models.CharField(max_length=50, null=True)),
                ('icon_background_color', models.CharField(max_length=10, null=True)),
                ('icon_mask_base_uri', models.URLField(null=True)),
                ('open_now', models.BooleanField(default=False)),
                ('reference', models.CharField(max_length=50, null=True)),
                ('scope', models.CharField(max_length=50, null=True)),
                ('types', models.TextField(null=True)),
                ('vicinity', models.CharField(max_length=255, null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='hotels_city', to='trip.city')),
                ('geometry', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='trip.geometry')),
            ],
            options={
                'verbose_name': 'Hotel',
                'verbose_name_plural': 'Hotels',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(null=True)),
                ('lng', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.CharField(max_length=200)),
            ],
            options={
                'db_table': '"media"',
            },
        ),
        migrations.CreateModel(
            name='Park',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(null=True), default=list, size=None)),
                ('meta_data', models.JSONField(default=dict)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='park_city', to='trip.city')),
            ],
            options={
                'verbose_name': 'Park',
                'verbose_name_plural': 'Parks',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('html_attributions', models.TextField()),
                ('photo_reference', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PlusCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compound_code', models.CharField(max_length=250)),
                ('global_code', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'db_table': '"status"',
            },
        ),
        migrations.CreateModel(
            name='Viewport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('northeast_lat', models.FloatField(null=True)),
                ('northeast_lng', models.FloatField(null=True)),
                ('southwest_lat', models.FloatField(null=True)),
                ('southwest_lng', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='WeirdAndWacky',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(null=True), default=list, size=None)),
                ('meta_data', models.JSONField(default=dict)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='weirdandwacky_city', to='trip.city')),
            ],
            options={
                'verbose_name': 'Weird And Wacky',
                'verbose_name_plural': 'Weird And Wacky',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='UserLikes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_attractions', models.ManyToManyField(to='trip.attraction')),
                ('liked_events', models.ManyToManyField(to='trip.event')),
                ('liked_extremesports', models.ManyToManyField(to='trip.extremesport')),
                ('liked_historicalsites', models.ManyToManyField(to='trip.historicalsite')),
                ('liked_hotels', models.ManyToManyField(to='trip.hotel')),
                ('liked_parks', models.ManyToManyField(to='trip.park')),
                ('liked_wierdandwacky', models.ManyToManyField(to='trip.weirdandwacky')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='hotel',
            name='media',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trip.media'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='photos',
            field=models.ManyToManyField(to='trip.photo'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='plus_code',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='trip.pluscode'),
        ),
        migrations.AddField(
            model_name='geometry',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='trip.location'),
        ),
        migrations.AddField(
            model_name='geometry',
            name='viewport',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='trip.viewport'),
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(null=True), default=list, size=None)),
                ('meta_data', models.JSONField(default=dict)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food_city', to='trip.city')),
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
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(null=True), default=list, size=None)),
                ('meta_data', models.JSONField(default=dict)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='familyfun_city', to='trip.city')),
            ],
            options={
                'verbose_name': 'Family Fun',
                'verbose_name_plural': 'Family Fun',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='DriveWebsite',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('url_link', models.URLField(blank=True, max_length=500, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='website_category', to='trip.category')),
            ],
            options={
                'verbose_name': 'DriveWebsite',
                'verbose_name_plural': 'DriveWebsites',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('images', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(null=True), default=list, size=None)),
                ('meta_data', models.JSONField(default=dict)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camp_city', to='trip.city')),
            ],
            options={
                'verbose_name': 'Camp',
                'verbose_name_plural': 'Camps',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='attraction',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attraction_city', to='trip.city'),
        ),
    ]
