from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'^next_song/(?P<station_id>\d+)/$', views.view_next_song),
    url(r'^neighbor_stations/(?P<latitude>\d+\.\d+)/(?P<longitude>\d+\.\d+)/$', views.view_neighbor_stations),
]