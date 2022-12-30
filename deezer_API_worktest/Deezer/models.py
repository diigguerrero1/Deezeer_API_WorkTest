from django.db import models


class Artist(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    pub_date = models.DateTimeField("Fecha Publicación", auto_now_add=True)
    picture = models.CharField(max_length=300, blank=True)
    status = models.BooleanField('Activo/No Activo', default=True)
    type = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Artist'
        verbose_name_plural = 'Artists'

    def __str__(self):
        return self.name

    
class Album(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    pub_date = models.DateTimeField("Fecha Publicación", auto_now_add=True)
    picture = models.CharField(max_length=300, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    status = models.BooleanField('Activo/No Activo', default=True)
    tracklist = models.CharField("URL del tracklist", max_length=300, blank=True)
    type = models.CharField(max_length=50, blank=True)


    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'

    def __str__(self):
        return self.title


class Song(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    pub_date = models.DateTimeField("Fecha Publicación")
    picture = models.CharField(max_length=300, blank=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    status = models.BooleanField('Activo/No Activo', default=True)
    link = models.CharField("URL de la canción", max_length=300, blank=True)
    duration = models.IntegerField("duración del album", blank=True)
    type = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Song'
        verbose_name_plural = 'Songs'

    def __str__(self):
        return self.title