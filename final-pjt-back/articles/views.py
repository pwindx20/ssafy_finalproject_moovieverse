from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Article, Comment, Category
from .serializers import (
    ArticleListSerializer, 
    ArticleSerializer, 
    ArticleDetailSerializer, 
    CommentSerializer,
    CategorySerializer
)
from movies.models import Movie
from movies.serializers import MovieTitleSerializer

# 카테고리 생성용
# @api_view(['POST'])
# def category(request):
#     if request.method=='POST':
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# 전체 게시글 목록/ 게시글 생성
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data['movie'])
        print(type(request.data['movie']))
        if ((request.data['category']==2) & (request.data['movie'] != None)) or ((request.data['category']!=2) & (request.data['movie'] == None)):
            print('통과했나?')
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)  
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('안했다')
            data = {
                'err': '잘못된 입력입니다.'
            }
            return Response(data)
            
# 카테고리별 게시글 목록
@api_view(['GET'])
def category_list(request, category_id):
    articles = Article.objects.all().filter(category=category_id)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)


# 영화별 게시글 목록
@api_view(['GET'])
def movie_list(request, movie_id):
    articles = Article.objects.all().filter(movie=movie_id)
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)


# 게시글 조회/수정/삭제
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)

    if request.method == 'GET':
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete': f'게시글 {article_id}번이 삭제되었습니다.'
        }  
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    

# 게시글 좋아요
@api_view(['POST'])
def article_likes(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.user != article.user:
        if request.user in article.article_liked_user.all():
            article.article_liked_user.remove(request.user)
            article_like = False
        else:
            article.article_liked_user.add(request.user)
            article_like = True
        data = {
            'article_like': article_like,
        }
        return Response(data)
    data = {
        'error': '본인의 게시글에는 좋아요할 수 없습니다.'
    }
    return Response(data)

# 댓글 생성
@api_view(['POST'])
def comment_create(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, article=article)
            return Response(serializer.data)


# 댓글 수정/삭제 
@api_view(['PUT', 'DELETE'])
def comment_detail(request, article_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete': f'댓글 {comment_id}번이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)