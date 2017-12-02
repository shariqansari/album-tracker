from __future__ import unicode_literals

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models

class Artist(models.Model):
    user        = models.OneToOneField(settings.AUTH_USER_MODEL)
    name        = models.CharField(max_length=255)

    def __str__(self):
        return u"{}".format(self.name)


class Album(models.Model):
    number = models.IntegerField
    title  = models.CharField(max_length=255)

    def __str__(self):
        return u"{}".format(self.title)

    def get_absolute_url(self):
        return reverse('album-detail', kwargs={'pk': self.id})

class Track(models.Model):
    album       = models.ForeignKey(Album, related_name="tracks")
    title       = models.CharField(max_length=255)
    finalized   = models.BooleanField(default=False)
    artists     = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return u"{}".format(self.title)

    def get_absolute_url(self):
        return reverse('track-detail', kwargs={'pk': self.id})

    def revisions(self):
        return self.revision_set.all().order_by('-upload_date')

    def latest(self):
        try:
            return self.revision_set.all().order_by('-upload_date')[0:1].get()
        except:
            pass
        return None

class Source(models.Model):
    title       = models.CharField(max_length=255)
    url         = models.URLField(max_length=255)
    track       = models.ForeignKey(Track, related_name="sources")

    def __str__(self):
        return u"{}".format(self.title)

class Revision(models.Model):
    track       = models.ForeignKey(Track)
    upload_date = models.DateTimeField(auto_now_add=True)
    file        = models.FileField()
    approved    = models.BooleanField(default=False)

    def __str__(self):
        return u"{} {}".format(self.track, self.upload_date)
