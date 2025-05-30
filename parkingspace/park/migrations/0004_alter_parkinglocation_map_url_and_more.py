# Generated by Django 5.2 on 2025-05-01 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0003_parkinglocation_map_url_parkinglocation_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parkinglocation',
            name='map_url',
            field=models.URLField(default='https://www.google.com/maps?q=41.09599179259704,29.092028542328315'),
        ),
        migrations.AlterField(
            model_name='parkinglocation',
            name='video_url',
            field=models.URLField(default='https://www.youtube.com/watch?v=dQw4w9WgXcQ'),
        ),
    ]
