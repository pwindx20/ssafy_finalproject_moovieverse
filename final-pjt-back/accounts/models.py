from django.db import models
from django.contrib.auth.models import AbstractUser
from articles.models import Article
from movies.models import Genre, Movie, Review, Playlist
from allauth.account.adapter import DefaultAccountAdapter
    
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=150)
    email = models.EmailField(max_length=254, null=True, blank=True)
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    watch_movie = models.ManyToManyField(Movie, related_name='movie_watched_user')
    like_review = models.ManyToManyField(Review, related_name='review_liked_user')
    like_playlist = models.ManyToManyField(Playlist, related_name='playlist_liked_user')
    like_article = models.ManyToManyField(Article, related_name='article_liked_user')
    
    USERNAME_FIELD = 'username'
    
class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
    
        from allauth.account.utils import user_email, user_field, user_username
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        nickname = data.get("nickname")
        
        user_email(user, email)
        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, "nickname", nickname)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()
        return user