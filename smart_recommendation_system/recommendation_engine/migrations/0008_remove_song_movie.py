# Generated by Django 5.0.1 on 2024-06-15 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation_engine', '0007_rename_songs_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='movie',
        ),
    ]
