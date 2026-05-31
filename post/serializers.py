from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'created_at', 'updated_at']

class PostWithAuthorIdSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author_id', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        author_id = validated_data.pop('author_id')
        author = User.objects.get(id=author_id)
        post = Post.objects.create(author=author, **validated_data)
        return post
    
    def update(self, instance, validated_data):
        if 'author_id' in validated_data:
            author_id = validated_data.pop('author_id')
            instance.author = User.objects.get(id=author_id)
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance