"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.artist_list, name='artist_list'),
    path('artist/<str:artist_name>/', views.tracks_list, name='artist'),
    path('album/', views.album_list, name='album_list'),
    path('album/<str:album_name>/', views.album_list_track, name='album'),
    path('genre/', views.genge_list, name='genre_list'),
    path('genre/<str:genre_name>/', views.genre_list_track, name='genre'),
]
