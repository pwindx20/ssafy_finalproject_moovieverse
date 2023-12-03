from django.contrib import admin
from .models import Genre, Movie, Playlist

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Playlist)
# admin.site.register(LikeMovie)