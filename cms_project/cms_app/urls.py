# cms_app/urls.py

from django.urls import path, include
from .views import UserAPIView, PostAPIView, LikeAPIView


urlpatterns = [
    path('user', UserAPIView.as_view()),
    path('user/<str:pk>', UserAPIView.as_view()),\
    path('post', PostAPIView.as_view()),
    path('post/<str:pk>', PostAPIView.as_view()),
    path('like', LikeAPIView.as_view()),
    path('like/<str:pk>', LikeAPIView.as_view()),
]
