from django.db import models
from MixtapeServeur.apps.station.models import Station
from MixtapeServeur.apps.artiste.models import Artiste
from MixtapeServeur.apps.taste.models import Taste
from MixtapeServeur.apps.genre.models import Genre

class MixtapeUser(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.IntegerField()
    station = models.ForeignKey(Station)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    
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

def general_taste(mixtape_user_id):
    """
    docstring
    """
    mixtape_user = MixtapeUser.objects.get(pk=mixtape_user_id)
    general_taste_dic = {}
    for taste in Taste.objects.filter(mixtapeUser=mixtape_user):
        if taste.points == 200: # it was a liked genre
            if taste.genre.nom in general_taste_dic:
                general_taste_dic[taste.genre.nom] += 200
            else:
                general_taste_dic[taste.genre.nom] = 200
        if taste.points == 100: # it was a liked artiste
            if taste.artiste.genre.nom in general_taste_dic:
                general_taste_dic[taste.genre.nom] += 100
            else:
                general_taste_dic[taste.genre.nom] = 100
        if taste.points == -200: # it was a unliked genre
            if taste.genre.nom in general_taste_dic:
                general_taste_dic[taste.genre.nom] += -200
            else:
                general_taste_dic[taste.genre.nom] = -200
    #  once we know the teste of the user we turn it into purcentage 
        total_point = 0
        for value in general_taste_dic.values():
            total_point = abs(value)
        ratio = total_point / 100
        for key in general_taste_dic.keys():
            general_taste_dic[key] /= ratio
        return general_taste_dic

