# Generated by Django 3.2.7 on 2021-10-05 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userfavoritesong',
            old_name='favourite_playlist',
            new_name='favourite_song',
        ),
    ]
