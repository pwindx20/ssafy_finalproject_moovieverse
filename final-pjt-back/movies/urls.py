from django.urls import path
from . import views
urlpatterns = [
    # 영화 단어 검색
    path('search/', views.search),

    # 영화 장르 추천
    path('recommend/prefer/', views.genre_recommend),
    path('recommend/nprefer/', views.new_genre_recommend),
    
    # 단일 영화 조회
    path('<int:movie_id>/', views.movie_detail),
    # 영화 보고싶어요
    path('<int:movie_id>/watch/', views.movie_watch),
    
    # 랜덤 리뷰 조회
    path('reviews/', views.review_list),
    # 리뷰 생성/수정/삭제
    path('<int:movie_id>/reviews/', views.review_create),
    path('<int:movie_id>/reviews/<int:review_id>/', views.review_detail),
    # 리뷰 좋아요
    path('<int:movie_id>/reviews/<int:review_id>/likes/', views.review_likes),

    # 플레이리스트 생성
    path('playlists/', views.playlist_create),
    # 플레이리스트에 영화 추가
    path('playlists/<int:playlist_id>/add/<int:movie_id>/', views.playlist_movie_like),
    # 플레이리스트 조회/수정/삭제
    path('playlists/<int:playlist_id>/', views.playlist_detail),
    # 플레이리스트 좋아요
    path('playlists/<int:playlist_id>/likes/', views.playlist_likes),
    # 플레이리스트 추천 순 조회
    path('playlists/recommend/', views.playlist_recommend),
]   
