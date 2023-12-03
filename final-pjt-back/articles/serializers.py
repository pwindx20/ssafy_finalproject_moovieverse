from rest_framework import serializers
from .models import Article, Comment, Category
from movies.serializers import MovieTitleSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
    
        
class CommentSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', 'user',)
        
# 게시글 리스트    
class ArticleListSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    movie = MovieTitleSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    review_liked_user_count = serializers.IntegerField(source="article_liked_user.count", read_only=True)

    class Meta:
        model = Article
        exclude = ('content', 'updated_at',)
        read_only_fields = ('user',)
    

# 게시글 수정
class ArticleDetailSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    category = CategorySerializer(read_only=True)
    movie = MovieTitleSerializer(read_only=True)
    article_liked_user_count = serializers.IntegerField(source="article_liked_user.count", read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)
    
# 게시글 생성
class ArticleSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.nickname', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    article_liked_user_count = serializers.IntegerField(source="article_liked_user.count", read_only=True)
    
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)