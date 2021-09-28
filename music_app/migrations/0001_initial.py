# Generated by Django 3.2.7 on 2021-09-28 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStampedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='music_app.timestampedmodel')),
                ('name', models.CharField(max_length=50)),
            ],
            bases=('music_app.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='MusicGenre',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='music_app.timestampedmodel')),
                ('name', models.CharField(max_length=50)),
            ],
            bases=('music_app.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='music_app.timestampedmodel')),
                ('name', models.CharField(max_length=50)),
                ('artists', models.ManyToManyField(to='music_app.Artist')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.musicgenre')),
            ],
            bases=('music_app.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='UserFavoriteSong',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='music_app.timestampedmodel')),
                ('favourite_songs', models.ManyToManyField(to='music_app.Song')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('music_app.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='UserFavoritePlaylist',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='music_app.timestampedmodel')),
                ('favourite_songs', models.ManyToManyField(to='music_app.Song')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('music_app.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='music_app.timestampedmodel')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('songs', models.ManyToManyField(to='music_app.Song')),
            ],
            bases=('music_app.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='music_app.timestampedmodel')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('music_genre', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='music_app.musicgenre')),
                ('songs', models.ManyToManyField(to='music_app.Song')),
            ],
            bases=('music_app.timestampedmodel',),
        ),
    ]