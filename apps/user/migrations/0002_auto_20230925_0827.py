# Generated by Django 3.2 on 2023-09-25 08:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserVerification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('verification_type', models.CharField(choices=[('TOKEN', 'TOKEN'), ('OTP', 'OTP')], default='OTP', max_length=100)),
                ('verification_code', models.CharField(max_length=255)),
                ('expiry_time', models.DateTimeField()),
                ('is_used', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserVerification',
                'verbose_name_plural': 'UserVerifications',
                'ordering': ['-created_at'],
            },
        ),
        migrations.DeleteModel(
            name='VerificationToken',
        ),
    ]
