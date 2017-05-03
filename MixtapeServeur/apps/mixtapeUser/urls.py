from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^creat_mixtape_user$', views.creat_mixtape_user),
    url(r'^test_set_station$', views.test_set_station),
    url(r'^test_test_gen_taste$', views.test_test_gen_taste),
]