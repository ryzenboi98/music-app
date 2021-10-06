from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
'''

class Artist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class MusicGenre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=50)
    artists = models.ManyToManyField(Artist)
    genre = models.ForeignKey(MusicGenre, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Playlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=50)
    music_genre = models.ForeignKey(MusicGenre, default=None, null=True, blank=True, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    songs = models.ManyToManyField(Song)

    def __str__(self):
        return self.name

class UserFavoriteSong(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    favourite_songs = models.ManyToManyField(Song)







