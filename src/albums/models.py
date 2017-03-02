from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

ROLES = [(a, a) for a in 
    ('Creator', 'Director', 'Assistant Director', 'Cover Artist', 'Engineer', 'Quality Control', 'Artist')
    ]

class Series(models.Model):
    title = models.CharField(max_length=255)

class Volume(models.Model):
    series = models.ForeignKey(Series)
    number = models.IntegerField
    title = models.CharField(max_length=255)

    def artists(self):
        return self.staff.filter(role="Artist")

class Track(models.Model):
    volume = models.ForeignKey(Volume)
    title = models.CharField(max_length=255)
    primary_artist = models.ForeignKey(User)

class Staff(models.Model):
    role = models.CharField(max_length=20, choices=ROLES)
    volume = models.ForeignKey(Volume, related_name="staff")
