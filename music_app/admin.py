from django.contrib import admin
from music_app.models import *

# Register your models here.
admin.site.register(Artist)
admin.site.register(MusicGenre)
admin.site.register(Album)
admin.site.register(Playlist)
admin.site.register(Song)
admin.site.register(UserFavoriteSong)

