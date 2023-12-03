# Moovieverse
팀명: 지수와 코딩공장


https://www.notion.so/3143c7571e7e484699df32105d4c8e47?v=32e0231d2aba4f6b9ebfb50833df2080&pvs=4


1. 팀원 정보 및 업무 분담 내역

|이름|강지수|위세영|
|-|-|-|
|업무|백엔드(Django)|프론트엔드(Vue3)|

<br>

![업무상세](docs/업무%20상세.PNG)


2. 목표 서비스 구현 및 실제 구현 정도

> 영화
- 영화 검색
- 영화 상세 정보 조회
- 영화 보고싶어요 기능
- 영화별 한줄평 작성
- 한줄평 좋아요 기능
- 장르 기반 영화 추천 알고리즘
- 랜덤 한줄평 조회
> 게시글
- 카테고리별 게시판 조회
- 게시판 상세 정보 조회
- 게시글 댓글 작성
- 게시글 좋아요 기능




![로고](/docs/rn_image_picker_lib_temp_b2928ac1-326a-4101-a9e9-2936da60777a.png)



3. 데이터베이스 모델링

#### ERD

#### 컴포넌트 구조도
![컴포넌트](/docs/moovieverse%20컴포넌트%20구조도.drawio.png)

#### url 설계도
```
# accounts.urls

urlpatterns = [
    # # 회원가입
    # path('registration/', include('dj_rest_auth.registration.urls')),
    # # 로그인
    # path('login/', include('dj_rest_auth.urls')),
    # # 로그아웃
    # path('logout/', include('dj_rest_auth.urls')),
    # # 회원정보 수정
    # path('user/',include('dj_rest_auth.urls')),
    # # 비밀번호 변경
    # path('password/change/', include('dj_rest_auth.urls')),
    # # 비밀번호 초기화
    # path('password/reset/',include('dj_rest_auth.urls')),
    # 프로필
    path('<username>/profile/', views.profile),
    # 팔로우
    path('<int:user_id>/follow/', views.follow),
]
```

```
# articles.urls

urlpatterns = [
    # 전체 게시글 목록/ 게시글 생성
    path('', views.article_list),
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

```

```
# movies.urls
 
urlpatterns = [
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

    # 플레이리스트 전체조회/생성
    path('playlists/', views.playlist_create),
    # 플레이리스트 조회/수정/삭제
    path('playlists/<int:playlist_id>/', views.playlist_detail),
    # 플레이리스트 좋아요
    path('playlists/<int:playlist_id>/likes', views.playlist_likes),
    # 플레이리스트 추천 순 조회
    path('playlists/recommend/', views.playlist_likes),
]   
```


4. 영화 추천 알고리즘에 대한 기술적 설명

- 장르 기반 선호 장르/ 비선호 장르 추천
    - 대상자의 review를 전부 가져옴
    - review에 연결된 장르에 review rank 점수를 더해 조화평균을 구함
    - 가장 높은 점수가 나온 장르들을 모아 해당 장르의 영화를 랜덤으로 20개를 골라옴
    - 가장 낮은 점수(최저 0점) 장르들을 모아 해당 장르의 영화를 랜덤으로 20개를 골라옴

- 리뷰 랜덤 조회(추천)
    - 영화 10개를 임의로 골라 그 중 리뷰 하나를 무작위로 뽑는다. (만약 영화 중 리뷰가 하나도 없을 시 다른 영화를 무작위로 추가)
    

5. 서비스 대표 기능에 대한 설명
- 리뷰를 랜덤으로 보여줘 배경지식없이 영화를 선택할 수 있다.
- 장르기반 추천을 통해 평소 보던 장르, 평소에 보지 않는 장르를 추천받을 수 있다.
- 카테고리별 게시판이 구성
- 영화 검색 기능
- 프로필 페이지에 보고싶은 영화/ 좋아요를 누른 게시글, 리뷰, 댓글/ 내가 쓴 게시글, 리뷰, 댓글을 볼 수 있음

7. 기타(느낀점, 후기 등)
- 깃 관리의 중요성
    - 기능 하나당 git을 push하고 pull을 해야 충돌이 나지 않는다.
- 프론트엔드와 백엔드 간의 원활한 소통의 중요성
    - 백엔드에서 제공하는 함수, 데이터에 대한 설명 부족으로 프론트 함수에서 오류가 많이 발생함
- 프로그래밍 변수 명명법의 중요성
    - ex. 케밥케이스, 스네이크케이스, 파스칼케이스, 카멜케이스