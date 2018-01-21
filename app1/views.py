from django.shortcuts import render
from django.http import Http404
from .models import Artist, Genre, Album
from .filters import ArtistFilter, GenreFilter

def artist_list(request):
    artist_list = Artist.objects.all()
    artist_filter = ArtistFilter(request.GET, queryset=artist_list)
    return render(request, 'app1/artist.html', {'filter': artist_filter})

def tracks_list(request, artist_name):
    try:
        artist = Artist.objects.get(name=artist_name)
        albums = Album.objects.filter(tracks_of_album__artist=artist).values('name').distinct()
    except Artist.DoesNotExist:
        raise Http404
    return render(request, 'app1/tracks.html', {
        'tracks': artist.tracks_of_artist.select_related(),
        'artist': artist,
        'albums': albums,

    })
def genre_list_track(request, genre_name):
    try:
        genre = Genre.objects.get(name=genre_name)
    except Genre.DoesNotExist:
        raise Http404
    return  render(request, 'app1/genre.html', {
        'genre': genre,
        'tracks': genre.tracks_of_genre.select_related()
    })
def genge_list(request):
    genre = Genre.objects.all()
    genre_filter = GenreFilter(request.GET, queryset=genre)
    return render(request, 'app1/genre_list.html', {'filter': genre_filter})

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'app1/album_list.html', {'albums': albums})

def album_list_track(request, album_name):
    try:
        album = Album.objects.get(name=album_name)
    except Genre.DoesNotExist:
        raise Http404
    return  render(request, 'app1/album.html', {
        'album': album,
        'tracks': album.tracks_of_album.select_related()
    })