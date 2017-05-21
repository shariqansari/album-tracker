from django.shortcuts import render
from django.views.generic import ListView, DetailView

from . import models

class AlbumList(ListView):
	model = models.Album

class AlbumDetail(DetailView):
	model = models.Album
	
class TrackDetail(DetailView):
	model = models.Track
	