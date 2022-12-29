
from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin


from .models import *




class ArtistResource(resources.ModelResource):
    class Meta:
        model = Artist

class ArtistAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name', 'status', 'pub_date')
    resource_class = ArtistResource

admin.site.register(Artist, ArtistAdmin)




class AlbumResource(resources.ModelResource):
    class Meta:
        model = Album

class AlbumAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'artist', 'pub_date')
    resource_class = AlbumResource

admin.site.register(Album, AlbumAdmin)




class SongResource(resources.ModelResource):
    class Meta:
        model = Song

class SongAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['title']
    list_display = ('title', 'artist', 'album', 'pub_date')
    resource_class = SongResource

admin.site.register(Song, SongAdmin)