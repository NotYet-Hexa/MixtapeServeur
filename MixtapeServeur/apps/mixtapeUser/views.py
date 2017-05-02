from django.http import HttpResponse
from django.shortcuts import render
from MixtapeServeur.apps.station.models import Station
from .models import MixtapeUser, set_station, creat_mixtape_user 
from .functions import test_dic_gen_taste, station_taste

def test_creat_MTuser(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    # code pour tester créer perso
    creat_mixtape_user("FN2", "LN2", 21, ["aa", "bb", "cc"], ["g1", "g2", "g3"], ["g4", "g5"], 1, 1)
    text = """<h1>Test creat user have been executed, check out if the user had been
     corectly created</h1>"""
    return HttpResponse(text)

def test_set_station(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    # code pour tester set station
    mixtape_user = MixtapeUser(fname="FN_test_set_station2", lname="LN_test_set_station2",
                               age=21, station=Station.objects.get(nom="NULL"), latitude=1,
                               longitude=1)
    mixtape_user.save()
    station = Station(nom="test_set_station2", latitude=1, longitude=1)
    station.save()
    set_station(mixtape_user.id, station.id)
    text = """<h1>Test set station have been executed, check out if the user had been
     corectly created</h1>"""
    return HttpResponse(text)

def test_test_gen_taste(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    # code pour tester créer 
    station_taste(station_id=6)
    text = """ <h1> Test </h1>"""
    return HttpResponse(text)

