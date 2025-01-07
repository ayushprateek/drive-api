# Generated by Django 4.1.7 on 2025-01-08 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0056_alter_photo_author_photo_uri_alter_photo_author_uri_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.TextField()),
                ('image_url', models.URLField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': '"keyword"',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='keywords_relation',
            field=models.ManyToManyField(related_name='categories', to='trip.keyword'),
        ),
    ]
