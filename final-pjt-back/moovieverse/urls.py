from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('articles/',include('articles.urls')),
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/registration/', include('dj_rest_auth.registration.urls')),
    # 프로필
    path('accounts/<username>/profile/', views.profile),
    # 팔로우
    path('accounts/<int:user_id>/follow/', views.follow),
    # 회원정보 수정
    path('accounts/update/', views.update),
]
