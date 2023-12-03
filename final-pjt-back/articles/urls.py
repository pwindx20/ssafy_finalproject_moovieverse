from django.urls import path
from . import views

urlpatterns = [
    # 전체 게시글 목록/ 게시글 생성
    path('', views.article_list),
    # 카테고리 생성용
    # path('category/', views.category),
    # 카테고리/영화별 게시글 목록
    path('category/<int:category_id>/', views.category_list),
    path('movie/<int:movie_id>/', views.movie_list),
    # 게시글 조회/수정/삭제
    path('<int:article_id>/', views.article_detail),
    # 게시글 좋아요
    path('<int:article_id>/likes/', views.article_likes),
    # 댓글 생성
    path('<int:article_id>/comments/', views.comment_create),
    # 댓글 수정/삭제
    path('<int:article_id>/comments/<int:comment_id>/', views.comment_detail),
]
