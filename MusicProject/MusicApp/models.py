from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Artist(TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class MusicGenre(TimeStampedModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Song(TimeStampedModel):
    name = models.CharField(max_length=50)
    artists = models.ManyToManyField(Artist)
    genre = models.ForeignKey(MusicGenre)

    def __str__(self):
        return self.name

class Playlist(TimeStampedModel):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name

class Album(TimeStampedModel):
    name = models.CharField(max_length=50)
    music_genre = models.ForeignKey(MusicGenre, default=None, null=True, blank=True)
    description = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name

class UserFavoriteSong(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favourite_songs = models.ManyToManyField(Song)

class UserFavoritePlaylist(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favourite_songs = models.ManyToManyField(Song)



