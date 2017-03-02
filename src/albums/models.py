from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from polymorphic.models import PolymorphicModel

ROLES = [(a, a) for a in (
        'Creator', 
        'Director', 
        'Assistant Director', 
        'Engineer', 
        'Quality Control', 
        'Primary Artist', 
        'Featured Artist',
        'Cover Artist', 
        )
    ]

class Series(models.Model):
    title = models.CharField(max_length=255)

class Volume(models.Model):
    series = models.ForeignKey(Series)
    number = models.IntegerField
    title = models.CharField(max_length=255)

class Track(models.Model):
    volume = models.ForeignKey(Volume)
    title = models.CharField(max_length=255)
    finalized = models.BooleanField(default=False)

class SourceTune(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

class Revision(models.Model):
    upload_date = models.DateTimeField(auto_now_add=True)
    file = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)

class Staff(PolymorphicModel):
    role = models.CharField(max_length=20, choices=ROLES)
    user = models.ForeignKey(User, related_name="roles")

class SeriesStaff(Staff):
    series = models.ForeignKey(Series, related_name="staff")

class VolumeStaff(Staff):
    volume = models.ForeignKey(Volume, related_name="staff")

class TrackStaff(Staff):
    track = models.ForeignKey(Track, related_name="staff")
