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



    