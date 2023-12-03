from rest_framework import serializers
from .models import Movie, Review, Genre, Playlist


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('content',)    
        read_only_fields = ('user',)


class ReviewSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    review_liked_user_count = serializers.IntegerField(source="review_liked_user.count", read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('user', 'movie',)

class MovieTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'poster_path')
        
        
class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only= True)
    review_set = ReviewSerializer(many=True, read_only=True)
    movie_watched_count = serializers.IntegerField(source="movie_watched_user.count", read_only=True)
    review_count = serializers.IntegerField(source="review_set.count", read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('like_users',)


        
class PlaylistSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    # likemovie_set = LikeMovieSerializer(many=True, read_only=True)
    like_movie = MovieTitleSerializer(many=True, read_only=True)
    movie_count = serializers.IntegerField(source='like_movie.count', read_only=True)
    playlist_liked_user_count = serializers.IntegerField(source='playlist_liked_user.count', read_only=True)    
    class Meta:
        model = Playlist
        fields = '__all__'
        read_only_fields = ('user',)

        
# class LikeMovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LikeMovie      
#         fields = '__all__'  
#         read_only_fields = ('playlist',)
        
########## 플레이리스트 serializer list형태로 받으려면...
# class PlaylistDetailSerializer(serializers.ModelSerializer):
#     # class movieSerializer(serializers.ModelSerializer):
#     #     class Meta:
#     #         model = Movie
#     #         fields = ('id',)
#     nickname = serializers.CharField(source='user.nickname', read_only=True)
#     # like_movies = serializers.ListField(child=serializers.IntegerField())
#     movie_count = serializers.IntegerField(source='like_movies.count', read_only=True)
#     playlist_liked_user_count = serializers.IntegerField(source='playlist_liked_user.count', read_only=True)
    
#     class Meta:
#         model = Playlist
#         fields = '__all__'
#         read_only_fields = ('user',)
        
        
        
        