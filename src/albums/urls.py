from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.AlbumList.as_view()),
    url(r'^(?P<pk>[-\w]+)/$', views.AlbumDetail.as_view(), name='album-detail'),
    url(r'^tracks/(?P<pk>[-\w]+)/$', views.TrackDetail.as_view(), name='track-detail'),    
]