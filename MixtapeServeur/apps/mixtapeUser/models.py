from django.db import models
from MixtapeServeur.apps.station.models import Station
from MixtapeServeur.apps.artiste.models import Artiste
from MixtapeServeur.apps.taste.models import Taste
from MixtapeServeur.apps.genre.models import Genre
import random


class MixtapeUser(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.IntegerField()
    station = models.ForeignKey(Station)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.fname+" "+self.lname 

def creat_mixtape_user(pfname, plname, page, pliked_artiste_list, pliked_genre_list,
                       punliked_genre_list, lat, longi):
    """
    pfname : string which contain the first name of the user
    plname : string which contain the laste name of the user
    page : int which contain the age of the user
    pliked_artiste_list : list of string which containe the name of the liked artiste
    pliked_genre_list : list of string which containe the name of the liked genre
    punliked_genre_list : list of string which containe the name of the unliked genre
    lat : int which contain the latitude of the user
    longi : int which contain the longitude of the user
    """
    mixtape_user = MixtapeUser(fname=pfname, lname=plname, age=page,
                               station=Station.objects.get(nom="NULL"), latitude=lat,
                               longitude=longi)
    mixtape_user.save()
    for liked_artiste in pliked_artiste_list:
        artiste = Artiste.objects.get(nom=liked_artiste)
        taste = Taste(points=100, genre=Genre.objects.get(nom="NULL"), artiste=artiste,
                      mixtapeUser=mixtape_user)
        taste.save()
    for liked_genre in pliked_genre_list:
        genre = Genre.objects.get(nom=liked_genre)
        taste = Taste(points=200, genre=genre, artiste=Artiste.objects.get(nom="NULL"),
                      mixtapeUser=mixtape_user)
        taste.save()
    for unliked_genre in punliked_genre_list:
        genre = Genre.objects.get(nom=unliked_genre)
        taste = Taste(points=-200, genre=genre, artiste=Artiste.objects.get(nom="NULL"),
                      mixtapeUser=mixtape_user)
        taste.save()

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






    

