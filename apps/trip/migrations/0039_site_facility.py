# Generated by Django 4.1.7 on 2024-12-13 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0038_site_show'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='facility',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
