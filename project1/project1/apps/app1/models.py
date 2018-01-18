from django.db import models
from django.utils.timezone import now

class Artist(models.Model):
    name = models.CharField('название', max_length=70)
    description = models.TextField('описание')
    data_of_career = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'артист'
        verbose_name_plural = 'артисты'

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('название',max_length=20)

    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'

    def __str__(self):
        return self.name


class Album(models.Model):
    name = models.CharField('название',max_length=30)
    data = models.DateField('дата выхода', blank=True, default=now)

    class Meta:
        verbose_name = 'альбом'
        verbose_name_plural = 'альбомы'

    def __str__(self):
        return self.name


class Track(models.Model):
    name = models.CharField('название', max_length=50)
    genre = models.ManyToManyField('Genre', related_name='tracks')
    album = models.ManyToManyField('Album', related_name='tracks')
    artist = models.ForeignKey(Artist, verbose_name='Артист', on_delete=models.DO_NOTHING, related_name='tracks')

    class Meta:
        verbose_name = 'трек'
        verbose_name_plural = 'треки'

    def __str__(self):
        return self.name
