from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel

class Album(models.Model):
    number = models.IntegerField
    title = models.CharField(max_length=255)

    def __str__(self):
    	return u"{}".format(self.title)

    def get_absolute_url(self):
    	return reverse('album-detail', kwargs={'pk': self.id})


class Track(models.Model):
    album = models.ForeignKey(Album, related_name="tracks")
    title = models.CharField(max_length=255)
    finalized = models.BooleanField(default=False)

    def get_absolute_url(self):
    	return reverse('track-detail', kwargs={'pk': self.id})

    def latest(self):
    	try:
    		return self.revisions.orderby('-upload_date')[0:1].get()
    	except:
    		return None

class Revision(models.Model):
    track = models.ForeignKey(Track, related_name="revisions")
    upload_date = models.DateTimeField(auto_now_add=True)
    file = models.FileField()
    approved = models.BooleanField(default=False)
