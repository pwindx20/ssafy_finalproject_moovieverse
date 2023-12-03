from django.contrib.auth import get_user_model
from rest_framework import serializers
from allauth.account.adapter import get_adapter
from dj_rest_auth.registration.serializers import RegisterSerializer


class UserSerializer(serializers.ModelSerializer):
    followings_count = serializers.IntegerField(source='followings.count', read_only=True)
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email', 'nickname', 'followings_count', 'followers_count')


# class UserFollowSerializer(serializers.ModelSerializer):
#     followings_count = serializers.IntegerField(source='followings.count', read_only=True)
#     followers_count = serializers.IntegerField(source='followers.count', read_only=True)

#     class Meta:
#         model = get_user_model()
#         fields = ('id', 'username', 'email', 'nickname', 'followings_count', 'followers_count')


class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=False, allow_blank=True, max_length=150)
    
    def get_cleaned_data(self):
        return {
            'username' : self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1',''),
            'email':self.validated_data.get('email', ''),
            'nickname': self.validated_data.get('nickname',''),
        }    
    
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user