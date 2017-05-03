from django.db import models

import random

from .models import Station
from MixtapeServeur.apps.mixtapeUser.models import MixtapeUser
from MixtapeServeur.apps.mixtapeUser.functions import station_taste
from MixtapeServeur.apps.music.models import Music




def get_list_of_user(the_station_id):
    """
    docstring
    """
    mixtape_user_list = []
    my_station = Station.objects.get(pk=the_station_id)
    for mixtape_user in MixtapeUser.objects.filter(station=my_station):
        mixtape_user_list.insert(1,mixtape_user)
    return mixtape_user_list
        
        

def next_song(station_id):
    """
    docstring
    """
    mixtape_user_list = get_list_of_user(the_station_id=station_id)
    proposed_song = []
    no_proposed_music = 1
    genre_dic =  station_taste(station_id=station_id)
    print(genre_dic)
    print("mixtape_users")
    for mixtape_user in mixtape_user_list:
        music = Music.objects.filter(mixtapeUser=mixtape_user)
        if music.count() == 1:
            no_proposed_music *=0
            music = music.first()
            if music.artiste.genre.nom in genre_dic.keys():
                i = 0
                while i <=  genre_dic[music.artiste.genre.nom]:
                    i +=1
                    proposed_song.insert(1,music.nom)
            else:
                proposed_song.insert(1,music.nom)
    if no_proposed_music != 1:
        print("proposed_song")
        print(proposed_song[random.randint(0, len(proposed_song)-1)])
        return proposed_song[random.randint(0, len(proposed_song)-1)]
    else:
        return "NULL"

def neighbor_stations(lat, longi):
    """
    doc
    """
    list_station_near = []
    stations = Station.objects.all()
    for station in stations:
        distance = ((station.latitude - float(lat))**2+
                    (station.longitude - float(longi))**2)
        if distance < ((10**(-6))):
            list_station_near.insert(1,station)
    return list_station_near
    

