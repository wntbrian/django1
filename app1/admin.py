from django.contrib import admin
from app1.models import Artist, Album, Track, Genre

admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Track)
admin.site.register(Genre)