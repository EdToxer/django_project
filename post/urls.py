from django.urls import path
from .views import PostListAPIView, PostDetailAPIView, PostCreateAPIView, PostUpdateAPIView, PostDeleteAPIView

urlpatterns = [
    path('', PostListAPIView.as_view(), name='post-list'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('create/', PostCreateAPIView.as_view(), name='post-create'),
    path('<int:pk>/update/', PostUpdateAPIView.as_view(), name='post-update'),
    path('<int:pk>/delete/', PostDeleteAPIView.as_view(), name='post-delete'),
]