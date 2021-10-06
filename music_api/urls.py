from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from music_app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'music-genres', views.MusicGenreViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'songs', views.SongViewSet)
router.register(r'playlists', views.PlaylistViewSet)
router.register(r'albums', views.AlbumViewSet)
router.register(r'favourite_songs', views.UserFavSongViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    #path('api/favourite_songs/', views.UserFavSongAPIView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]