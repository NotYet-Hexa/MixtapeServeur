from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^add_music_suggestion$', views.view_add_music_suggestion),
]