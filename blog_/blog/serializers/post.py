from rest_framework import serializers
from ..models import Post
from ..serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
  user = UserSerializer()
  class Meta:
    model = Post
    fields = ('id', "title", "description", "user","date")


class PostCreateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ("title", "description", "user", "date")

class PostUpdateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ("title", "description", "user","date")

