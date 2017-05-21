from django.contrib import admin
from . import models

class TrackInlineAdmin(admin.StackedInline):
	model = models.Track
	extra = 0

class AlbumAdmin(admin.ModelAdmin):
    inlines = [TrackInlineAdmin]

admin.site.register(models.Album, AlbumAdmin)