from django.urls import path, include
from . import views

urlpatterns = [
    path('chat/', views.chat, name='video_chat'),
    path('join/', views.join, name='video_chat_join'),
    path('get_token/', views.get_token),
    path('get_app_id/', views.get_app_id),
]
