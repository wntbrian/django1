from django.shortcuts import render
from django.http import Http404
from .models import Artist, Genre


def artist_list(request):
    artists = Artist.objects.filter(name__contains="")
    return render(request, 'app1/index.html', {'artists': artists})

def tracks_list(request, artist_name):
    try:
        artist = Artist.objects.get(name=artist_name)
    except Artist.DoesNotExist:
        raise Http404
    return render(request, 'app1/tracks.html', {
        'tracks': artist.tracks_of_artist.select_related(),
        'artist': artist,
    })
def genre_list(request, genre_name):
    try:
        genre = Genre.objects.get(name=genre_name)
    except Genre.DoesNotExist:
        raise Http404
    return  render(request, 'app1/genre.html', {
        'genre': genre,
        'tracks': genre.tracks_of_genre.select_related()
    })