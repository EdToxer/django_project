from django.urls import path
from .views import (
    CommentListAPIView, 
    CommentDetailAPIView, 
    PostCommentsAPIView,
    CommentCreateAPIView,
    CommentUpdateAPIView,
    CommentDeleteAPIView
)

urlpatterns = [
    # GET /comments - список всех комментариев
    path('comments', CommentListAPIView.as_view(), name='comment-list'),
    
    # GET /comments/<id> - детали комментария
    path('comment/<int:pk>', CommentDetailAPIView.as_view(), name='comment-detail'),
    
    # GET /posts/<post_id>/comments - комментарии поста
    path('posts/<int:post_id>/comments', PostCommentsAPIView.as_view(), name='post-comments'),
    
    # POST /comment/create - создание комментария
    path('comment/create', CommentCreateAPIView.as_view(), name='comment-create'),
    
    # POST /comment/update/<id> - обновление через POST
    path('comment/update/<int:pk>', CommentUpdateAPIView.as_view(), name='comment-update'),
    
    # POST /comment/delete/<id> - удаление через POST
    path('comment/delete/<int:pk>', CommentDeleteAPIView.as_view(), name='comment-delete'),
]