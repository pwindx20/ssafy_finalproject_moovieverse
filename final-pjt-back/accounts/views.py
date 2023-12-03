from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from movies.serializers import MovieTitleSerializer, ReviewSerializer, PlaylistSerializer
from articles.serializers import ArticleListSerializer, CommentSerializer

@api_view(['PUT'])
def update(request):
    me = request.user
    if request.method == 'PUT':
        serializer = UserSerializer(me, data=request.data)        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET'])
def profile(request, username):
    User = get_user_model()
    person = get_object_or_404(User, username=username)
    userSerializer = UserSerializer(person)

    movies = person.watch_movie.all()
    movieSerializer = MovieTitleSerializer(movies, many=True)
    print(person)

    my_reviews = person.review_set.all()
    myreviewSerializer = ReviewSerializer(my_reviews, many=True)
    
    reviews = person.like_review.all()
    reviewSerializer = ReviewSerializer(reviews, many=True)

    my_playlists = person.playlist_set.all()
    myplaylistSerializer = PlaylistSerializer(my_playlists, many=True)

    playlists = person.like_playlist.all()
    playlistSerializer = PlaylistSerializer(playlists, many=True)


    my_articles = person.article_set.all()
    myarticleSerializer = ArticleListSerializer(my_articles, many=True)
    
    articles = person.like_article.all()
    articleSerializer = ArticleListSerializer(articles, many=True)

    my_comments = person.comment_set.all()
    mycommentSerializer = CommentSerializer(my_comments, many=True)

    data = {
        'userSerializer': userSerializer.data,
        'movieSerializer': movieSerializer.data,
        'reviewSerializer': reviewSerializer.data,
        'playlistSerializer': playlistSerializer.data,
        'articleSerializer': articleSerializer.data,
        'myreviewSerializer': myreviewSerializer.data,
        'myplaylistSerializer': myplaylistSerializer.data,
        'myarticleSerializer' : myarticleSerializer.data,
        'mycommentSerializer': mycommentSerializer.data,
    }
    
    return Response(data)

@api_view(['POST'])
def follow(request, user_id):
    User = get_user_model()
    me = request.user
    you = get_object_or_404(User, pk=user_id)

    if me != you:
        if me in you.followers.all():
            you.followers.remove(me)
            isFollowed = False
        else:
            you.followers.add(me)
            isFollowed = True
        data = {
            'isFollowed': isFollowed,
            'followers_count': you.followers.count(),
            'followings_count': you.followings.count(),
        }
        return JsonResponse(data)

