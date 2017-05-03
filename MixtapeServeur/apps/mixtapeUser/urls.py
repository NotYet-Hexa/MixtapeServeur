from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^creat_mixtape_user$', views.creat_mixtape_user),
    url(r'^set_station$', views.view_set_station),
]