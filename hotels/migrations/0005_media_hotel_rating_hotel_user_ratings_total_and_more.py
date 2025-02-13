# Generated by Django 4.1.7 on 2024-05-29 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0004_alter_hotel_icon'),
    ]

    operations = [
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
        migrations.AddField(
            model_name='hotel',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='hotel',
            name='user_ratings_total',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='HotelMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
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
            name='media',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.media'),
        ),
    ]
