from django.conf.urls import url
from . import views


urlpatterns = [
    
    url(r'^next_song$', views.view_next_song),
    url(r'^exist$', views.exist),
    url(r'^neighbor_stations$', views.view_neighbor_stations),
]