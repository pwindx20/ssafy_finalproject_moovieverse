from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Movie, Review, Genre, Playlist
from .serializers import GenreSerializer, ReviewSerializer, MovieTitleSerializer, MovieSerializer, PlaylistSerializer
import random



# 단어 검색
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def search(request):
    if request.method=='POST':
        searched = request.data['searched'] # searched 라는 키로 data 보내야함
        movies = Movie.objects.filter(title__contains=searched)
        serializer = MovieTitleSerializer(movies, many=True)
        return Response(serializer.data)
    
fg = []

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def genre_recommend(request):
    global fg
    me = request.user
    reviews = me.review_set.all()

    if reviews.count() != 0:
        serializer = ReviewSerializer(reviews, many=True)

        analyze_genre = {}
        analyze_genre_count = {}
        favorite_genres = []
        favorite_genres_movie = []

        for review in serializer.data:
            movie = Movie.objects.get(pk=review['movie'])
            movie_serializer = MovieSerializer(movie)

            for genre in movie_serializer.data['genres']:
                if genre['name'] in analyze_genre:
                    analyze_genre[genre['name']] += 1/(review['rank'])
                    analyze_genre_count[genre['name']] += 1
                else:
                    analyze_genre[genre['name']] = 1/(review['rank'])
                    analyze_genre_count[genre['name']] = 1

        max_value = 0
        
        for k, v in analyze_genre.items():
            analyze_genre[k] = analyze_genre[k]/analyze_genre_count[k]
            if max_value< analyze_genre[k]:
                max_value = analyze_genre[k]
        
        for k, v in analyze_genre.items():
            if v==max_value:
                favorite_genres.append(k)
            
        # 외부 변경
        # #########################################
        # fg = []    
        # for i in favorite_genres:
        #     temp = Genre.objects.get(name=i)
        #     temps = GenreSerializer(temp).data['id']
        #     fg.append(temps)
        #############################################
        
        for genre_name in favorite_genres:
            f_genre = Genre.objects.get(name=genre_name)
            movies = f_genre.movie_set.all()
            m = MovieTitleSerializer(movies, many=True)        
            favorite_genres_movie += m.data
        
        random.shuffle(favorite_genres_movie)
        
        data = {
            'favorite_genres': favorite_genres,
            'favorite_genres_movie':favorite_genres_movie[:20]
        }
        return Response(data)

    else:
        movies = Movie.objects.order_by("?")
        serializer = MovieTitleSerializer(movies, many=True)

        return Response(serializer.data[:20])
    
    # INNER JOIN을 활용하면 좀더 간단하게 할 수 있음...


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def new_genre_recommend(request):
    global fg
    me = request.user
    reviews = me.review_set.all()

    if reviews.count() != 0:
        serializer = ReviewSerializer(reviews, many=True)
        analyze_genre = {}
        analyze_genre_count = {}
        challenge_genres = []
        challenge_genres_movie = []

        all_genres = Genre.objects.all()
        genres_serializer = GenreSerializer(all_genres, many=True)
        
        for g in genres_serializer.data:
            analyze_genre.setdefault(g['name'], 0)
            analyze_genre_count.setdefault(g['name'], 0)


        for review in serializer.data:
            movie = Movie.objects.get(pk=review['movie'])
            movie_serializer = MovieSerializer(movie)

            for genre in movie_serializer.data['genres']:
                if genre['name'] in analyze_genre:
                    analyze_genre[genre['name']] += 1/(review['rank'])
                    analyze_genre_count[genre['name']] += 1


        if list(analyze_genre.values()).count(0):
            min_value = 0
        
        else:
            min_value = 5        
            for k, v in analyze_genre.items():
                analyze_genre[k] = analyze_genre[k]/analyze_genre_count[k]
                if min_value> analyze_genre[k]:
                    min_value = analyze_genre[k]
            
        for k, v in analyze_genre.items():
            if v==min_value:
                challenge_genres.append(k)
        
        
        for genre_name in challenge_genres:
            f_genre = Genre.objects.get(name=genre_name)
            movies = f_genre.movie_set.all()
            # m = MovieSerializer(movies, many=True)        
            m = MovieTitleSerializer(movies, many=True)        
            challenge_genres_movie += m.data
        
        random.shuffle(challenge_genres_movie)
        
        data = {
            'challenge_genres': challenge_genres,
            'challenge_genres_movie':challenge_genres_movie[:20]
        }
        return Response(data)

    else:
        movies = Movie.objects.order_by("?")
        serializer = MovieTitleSerializer(movies, many=True)

        return Response(serializer.data[:20])


# 단일 영화 조회 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_detail(request, movie_id):
    
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
# 영화 보고싶어요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_watch(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if request.user in movie.movie_watched_user.all():
        movie.movie_watched_user.remove(request.user)
        movie_watch = False
    else:
        movie.movie_watched_user.add(request.user)
        movie_watch = True
    data = {
        'movie_watch': movie_watch,
    }
    return Response(data)


# 랜덤 리뷰 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def review_list(request):
    # movie를 랜덤으로 10개를 골라와 거기에 달린 리뷰 1개씩 무작위로 선별
    recommend_review = []
    movies_id = [m.id for m in Movie.objects.all()]

    random_movie_list = random.sample(movies_id, 10)
    for movie_id in random_movie_list:
        movie = Movie.objects.get(pk=movie_id)
        if movie.review_set.all().count():    
            review = movie.review_set.order_by("?").first()
            serializer = ReviewSerializer(review)
            recommend_review.append(serializer.data)
        else:
            while True:   
                temp = random.sample(movies_id, 1)[0]
                if temp not in random_movie_list:
                    random_movie_list.append(temp)
                    break                    

    
    return Response(recommend_review)


# 리뷰 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_create(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    # if request.method == 'POST':
    #     if Review.objects.get(user=request.user) in movie.review_set.all():
    #         data = {
    #             'err': '잘못된 접근입니다.'
    #         }
    #     else:
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 리뷰 수정, 삭제
@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def review_detail(request, movie_id, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
            
    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'리뷰 {review_id}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
# 리뷰 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def review_likes(request, movie_id, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.user != review.user:
        if request.user in review.review_liked_user.all():
            review.review_liked_user.remove(request.user)
            review_like = False
        else:
            review.review_liked_user.add(request.user)
            review_like = True
        data = {
            'review_like': review_like,
        }
        return Response(data)
    data = {
        'error': '본인의 리뷰에는 좋아요할 수 없습니다.'
    }
    return Response(data)


# 플레이리스트 추천 순 조회
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def playlist_recommend(request):
    if request.method == 'GET':
        playlists = Playlist.objects.all()
        serializer = PlaylistSerializer(playlists, many=True)
        ordered_data = sorted(serializer.data, key= lambda x : -x['playlist_liked_user_count'])
        datas = []
        for data in ordered_data:
            print(data['movie_count'])
            if data['movie_count'] != 0:
                datas.append(data)
        if len(datas) >5:
            datas = datas[:5]
                
        return Response(datas)
        

# 빈 플레이리스트 생성
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def playlist_create(request):
    if request.method == 'POST':
        serializer = PlaylistSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



# 플레이리스트에 영화 추가
@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def playlist_movie_like(request, playlist_id, movie_id):
    print(movie_id, playlist_id)
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    movie = get_object_or_404(Movie, pk=movie_id)
    
    if movie in playlist.like_movie.all():
        playlist.like_movie.remove(movie)
        choose_movie = False
    else:
        playlist.like_movie.add(movie)
        choose_movie = True
    data = {
        'choose_movie': choose_movie,
    }
    return Response(data)
    
    
# 플레이리스트 단일 조회/수정/삭제    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def playlist_detail(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    
    if request.method =='GET':
        serializer = PlaylistSerializer(playlist)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlaylistSerializer(playlist, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        playlist.delete()
        data = {
            'delete': f'플레이리스트 {playlist_id}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    
# 플레이리스트 좋아요
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def playlist_likes(request, playlist_id):
    playlist = get_object_or_404(Playlist, pk=playlist_id)
    if request.user in playlist.playlist_liked_user.all():
        playlist.playlist_liked_user.remove(request.user)
        playlist_like = False
    else:
        playlist.playlist_liked_user.add(request.user)
        playlist_like = True
    data = {
        'playlist_like': playlist_like,
    }
    return Response(data)
