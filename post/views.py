from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Post
from .serializers import PostSerializer, PostWithAuthorIdSerializer

class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostWithAuthorIdSerializer

@method_decorator(csrf_exempt, name='dispatch')
class PostUpdateAPIView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostWithAuthorIdSerializer
    
    # Переопределяем метод, чтобы он принимал POST вместо PUT/PATCH
    def post(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    # Опционально: если нужно частичное обновление через POST
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)  # True для частичного обновления
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        
        return Response({
            'status': 'success',
            'message': 'Post updated successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

@method_decorator(csrf_exempt, name='dispatch')
class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    # Переопределяем метод, чтобы он принимал POST вместо DELETE
    def post(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            'status': 'success',
            'message': 'Post deleted successfully'
        }, status=status.HTTP_200_OK)