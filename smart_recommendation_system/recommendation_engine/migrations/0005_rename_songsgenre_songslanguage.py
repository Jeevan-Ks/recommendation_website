# Generated by Django 5.0.1 on 2024-06-15 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation_engine', '0004_songsgenre_series_songs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SongsGenre',
            new_name='SongsLanguage',
        ),
    ]
