from django.db import models

from django.contrib.auth.models import AbstractUser

from MixtapeServeur.apps.station.models import Station
from MixtapeServeur.apps.artiste.models import Artiste
from MixtapeServeur.apps.taste.models import Taste
from MixtapeServeur.apps.genre.models import Genre
import random


class MixtapeUser(AbstractUser):
    is_facebook_user = models.BooleanField(max_length=100, default=False)
    fb_id = models.CharField(max_length=100, null=True, blank=True)
    profil_picture_url = models.CharField(max_length=100, null=True, blank=True)
    device = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, null=True, blank=True)
    token = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    station = models.ForeignKey(Station, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.get_full_name()



def set_station(mixtape_user_id, station_id):
    """
    station_name    : id of the station
    mixtape_user_id : id of the mixtape_user
    """
    mixtape_user = MixtapeUser.objects.get(pk=mixtape_user_id)
    mixtape_user.station = Station.objects.get(pk=station_id)
    mixtape_user.save()

def add_taste_genre(mixtape_user_id, genre_name): # A tester mais pas trop de risuqe vérifier si le genre existe deja 
    """
    genre_name      : name of the genre
    mixtape_user_id : id of the mixtape_user
    """
    mixtape_user = MixtapeUser.objects.get(pk=mixtape_user_id)
    new_genre = Genre.objects.get(nom=genre_name)
    null_artiste = Artiste.objects.get(nom="NULL")
    taste = Taste(points=200, genre=new_genre, artiste=null_artiste,
                  mixtapeUser=mixtape_user)
    taste.save()

    # faire del et idem pour artiste 






    

