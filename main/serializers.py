from rest_framework import serializers
from .models import Post,Comment,Category
from django.contrib.auth.models import User
from datetime import datetime
from rest_framework.authtoken.models import Token

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff','password')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')

class PostModelSerializer(serializers.ModelSerializer):
    owner = UserModelSerializer(read_only=True)
    category = CategoryModelSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'date', 'owner', 'category','like','img_src')

class CommentModelSerializer(serializers.ModelSerializer):
    owner = UserModelSerializer(read_only=True)
    post = PostModelSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ('id','comment','owner','post','date')













