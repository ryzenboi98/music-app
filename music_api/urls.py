from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from music_app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'music-genres', views.MusicGenreViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'songs', views.SongViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]