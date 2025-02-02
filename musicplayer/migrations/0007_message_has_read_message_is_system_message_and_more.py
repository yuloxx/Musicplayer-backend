# Generated by Django 5.0.6 on 2024-06-10 06:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicplayer', '0006_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='has_read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='is_system_message',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='musicplayer.ordinaryuser'),
        ),
    ]
