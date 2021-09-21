from rest_framework import serializers
from django.contrib.auth.models import User
# from .models import Comment
from .models import Post


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'first_name', 'last_name', 'email')


# class CommentSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = Comment
#     fields = ('id', 'who_posted', 'content')


class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('id', 'who_posted', 'approved', 'image', 'likes', 'liked_by', 'comments')
