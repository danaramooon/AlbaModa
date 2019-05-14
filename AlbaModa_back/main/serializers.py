from rest_framework import serializers
from .models import Post,Comment,Category,Product
from django.contrib.auth.models import User
from datetime import datetime
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=200)
    is_staff = serializers.BooleanField

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

# class UserModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'is_staff','password')
#
#     def create(self, validated_data):
#         user = User(
#             email=validated_data['email'],
#             username=validated_data['username']
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         Token.objects.create(user=user)
#         return user

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name')

class PostModelSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    category = CategoryModelSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'date', 'owner', 'category','like','img_src')

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    comment = serializers.CharField()
    owner = UserSerializer(read_only=True)
    post = PostModelSerializer(read_only=True)
    date = serializers.DateTimeField()

    def create(self, validated_data):
        c = Comment(**validated_data)
        c.save()
        return c

    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    price = serializers.IntegerField()
    img_src = serializers.CharField()

    def create(self, validated_data):
        p = Product(**validated_data)
        p.save()
        return p

    def update(self, instance, validated_data):
        instance.price = validated_data.get('price', instance.price)
        instance.save()
        return instance













