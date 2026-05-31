from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Comment
from .serializers import CommentSerializer, CommentCreateSerializer
from post.models import Post

class CommentListAPIView(generics.ListCreateAPIView):
    """Список всех комментариев или создание нового"""
    queryset = Comment.objects.all()
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentCreateSerializer
        return CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save()

class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """Получение, обновление, удаление конкретного комментария"""
    queryset = Comment.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return CommentCreateSerializer
        return CommentSerializer

class PostCommentsAPIView(generics.ListAPIView):
    """Получение всех комментариев для конкретного поста"""
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id).order_by('-created_at')

class CommentCreateAPIView(generics.CreateAPIView):
    """Создание комментария через POST"""
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

class CommentUpdateAPIView(generics.UpdateAPIView):
    """Обновление комментария (через POST если нужно)"""
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    
    # Для работы через POST вместо PUT/PATCH
    def post(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class CommentDeleteAPIView(generics.DestroyAPIView):
    """Удаление комментария (через POST если нужно)"""
    queryset = Comment.objects.all()
    
    # Для работы через POST вместо DELETE
    def post(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)