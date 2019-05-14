from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class PostManager(models.Manager):
    def for_user(self,owner):
        return self.filter(owner = owner)
    def category(self,category):
        return self.filter(category=category)

class CommentManager(models.Manager):
    def for_user(self,owner,comment):
        return self.filter(owner = owner,comment =comment)

    def for_post(self,post):
        return self.filter(post = post)

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="posts",null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts",null=True)
    date = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)
    img_src = models.CharField(max_length=200)
    my_post = PostManager()
    objects = models.Manager()

class Comment(models.Model):
    comment = models.TextField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name="comments",null=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comments")
    date = models.DateTimeField(auto_now_add=True)
    post_comment = CommentManager()
    objects = models.Manager()

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    img_src = models.CharField(max_length=200)

    def __str__(self):
        return self.name





