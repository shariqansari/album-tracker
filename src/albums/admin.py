from django.contrib import admin
from . import models

@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Track)
class TrackAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Source)
class SourceAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Revision)
class RevisionAdmin(admin.ModelAdmin):
    pass
