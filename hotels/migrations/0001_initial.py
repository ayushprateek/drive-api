# Generated by Django 4.1.7 on 2024-07-02 03:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': '"banner"',
            },
        ),
        migrations.CreateModel(
            name='Geometry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_status', models.CharField(max_length=50, null=True)),
                ('icon', models.URLField()),
                ('icon_background_color', models.CharField(max_length=10, null=True)),
                ('icon_mask_base_uri', models.URLField(null=True)),
                ('name', models.CharField(max_length=255)),
                ('open_now', models.BooleanField(default=False)),
                ('place_id', models.CharField(max_length=50)),
                ('rating', models.FloatField(null=True)),
                ('reference', models.CharField(max_length=50, null=True)),
                ('scope', models.CharField(max_length=50, null=True)),
                ('types', models.TextField(null=True)),
                ('user_ratings_total', models.IntegerField()),
                ('vicinity', models.CharField(max_length=255, null=True)),
                ('discount_url', models.CharField(max_length=400, null=True)),
                ('geometry', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.geometry')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(null=True)),
                ('lng', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.CharField(max_length=200)),
            ],
            options={
                'db_table': '"media_hotel_media"',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField()),
                ('width', models.IntegerField()),
                ('html_attributions', models.TextField()),
                ('photo_reference', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('trip_date', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': '"plan"',
            },
        ),
        migrations.CreateModel(
            name='PlusCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compound_code', models.CharField(max_length=50)),
                ('global_code', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'db_table': '"status_status"',
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': '"tax"',
            },
        ),
        migrations.CreateModel(
            name='Viewport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('northeast_lat', models.FloatField(null=True)),
                ('northeast_lng', models.FloatField(null=True)),
                ('southwest_lat', models.FloatField(null=True)),
                ('southwest_lng', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HotelMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(default=1)),
                ('position', models.IntegerField(default=1)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.hotel')),
                ('media', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.media')),
            ],
            options={
                'db_table': 'hotel_media',
            },
        ),
        migrations.AddField(
            model_name='hotel',
            name='photos',
            field=models.ManyToManyField(to='hotels.photo'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='plus_code',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.pluscode'),
        ),
        migrations.AddField(
            model_name='geometry',
            name='location',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hotels.location'),
        ),
        migrations.AddField(
            model_name='geometry',
            name='viewport',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hotels.viewport'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('token', models.CharField(max_length=250, null=True)),
                ('mobile', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('reward', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(null=True)),
                ('status', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.status')),
            ],
            options={
                'db_table': '"customer"',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('trip_date', models.DateTimeField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(null=True)),
                ('media', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.media')),
                ('status', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.status')),
            ],
            options={
                'db_table': '"category"',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=200)),
                ('url', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField(null=True)),
                ('status', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.status')),
            ],
            options={
                'db_table': '"article"',
            },
        ),
    ]
