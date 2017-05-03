from django.db import models
from MixtapeServeur.apps.station.models import Station
from MixtapeServeur.apps.artiste.models import Artiste
from MixtapeServeur.apps.taste.models import Taste
from MixtapeServeur.apps.genre.models import Genre
from .models import MixtapeUser
import random

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
        total_point += abs(value)
    ratio = total_point / 100

    for key in general_taste_dic.keys():
        general_taste_dic[key] /= ratio

    return general_taste_dic

def test_dic_gen_taste():
    mixtape_user_general_taste = general_taste(mixtape_user_id=9)


def station_taste(station_id):
    """
    docstring
    """
    the_station = Station.objects.get(pk=station_id)
    station_taste_dic = {}
    for mixtape_user in MixtapeUser.objects.filter(station=the_station):
        general_taste_dic = general_taste(mixtape_user_id=mixtape_user.id)
        for genre in general_taste_dic.keys():
            if genre in station_taste_dic.keys():
                station_taste_dic[genre] += general_taste_dic[genre]
            else:
                station_taste_dic[genre] = general_taste_dic[genre]
    prefered_genre_dic = {}
    i = 5
    while i > 0 :
        value_max = 0
        for genre, value in station_taste_dic.items():
            if value > value_max:
                genre_max = genre
                value_max = value
        prefered_genre_dic[genre_max] = (2*i)
        del station_taste_dic[genre_max]
        i-=1
    return prefered_genre_dic
    