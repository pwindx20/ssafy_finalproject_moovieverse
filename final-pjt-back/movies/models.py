from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
class Genre(models.Model):
    name = models.CharField(max_length=150)


class Movie(models.Model):
    title = models.CharField(max_length=150)
    overview = models.TextField()
    poster_path = models.CharField(max_length=1000, blank=True)
    production_countries = models.CharField(max_length=1000)
    release_date = models.DateField()
    runtime = models.IntegerField(validators=[MinValueValidator(0)])
    tagline = models.CharField(max_length=500, blank=True)
    genres = models.ManyToManyField(Genre)


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rank = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    content = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Playlist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    like_movie = models.ManyToManyField(Movie, related_name='movie_liked_playlist')  
    
# class LikeMovie(models.Model):
#     playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
#     movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    