from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^test_creat_MTuser$', views.test_creat_MTuser),
    url(r'^test_set_station$', views.test_set_station),

]