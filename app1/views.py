from django.shortcuts import render
from django.http import Http404
from .models import Artist


def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'app1/index.html', {'artists': artists})

def tracks_list(request, artist_name):
    try:
        artist = Artist.objects.get(name=artist_name)
    except Artist.DoesNotExist:
        raise Http404
    return render(request, 'app1/tracks.html', {
        'tracks': artist.tracks.all(),
        'artist': artist,
    })