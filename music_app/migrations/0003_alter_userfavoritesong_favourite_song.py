# Generated by Django 3.2.7 on 2021-10-05 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0002_rename_favourite_playlist_userfavoritesong_favourite_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavoritesong',
            name='favourite_song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.song'),
        ),
    ]
