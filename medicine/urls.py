from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.pill_dispenser, name='pill_dispenser'),
    path('about/', views.about, name='about'),
]
