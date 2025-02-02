# Generated by Django 5.0.6 on 2024-06-06 09:08

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicplayer', '0004_song_play_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Captcha',
            fields=[
                ('captchaId', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user_email', models.EmailField(max_length=254, unique=True)),
                ('captcha', models.CharField(max_length=10)),
                ('expire_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
