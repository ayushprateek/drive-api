# Generated by Django 4.1.7 on 2024-11-22 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0031_category_scrape_city_scrape'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='longitude',
            field=models.FloatField(null=True),
        ),
    ]
