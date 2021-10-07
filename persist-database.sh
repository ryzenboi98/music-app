#!/bin/bash

echo "Persisting data into database.."
python manage.py loaddata fixtures/artists.yaml
python manage.py loaddata fixtures/music_genres.yaml
python manage.py loaddata fixtures/songs.yaml