from rest_framework import serializers
from .models import Post, Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
            # all로 하면 id로 넘어감 


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('pk', 'title', 'content')
            # 필드 정해서 하면 pk에 들어감


class PostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Post
        fields = '__all__'



