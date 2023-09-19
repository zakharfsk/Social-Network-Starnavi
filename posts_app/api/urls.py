from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.CreatePostAPIView.as_view()),
    path('like/<int:pk>/', views.LikePostAPIView.as_view(), name='like_post'),
    path('unlike/<int:pk>/', views.UnlikePostAPIView.as_view(), name='unlike_post'),
    path('analytics/', views.PostLikesAnalytics.as_view(), name='post_analytics'),
]
