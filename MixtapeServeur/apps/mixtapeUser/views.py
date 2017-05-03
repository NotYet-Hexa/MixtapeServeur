import json

from django.http import HttpResponse, JsonResponse, HttpResponseForbidden

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from MixtapeServeur.apps.station.models import Station
from MixtapeServeur.apps.station.models import Station
from MixtapeServeur.apps.artiste.models import Artiste
from MixtapeServeur.apps.taste.models import Taste
from MixtapeServeur.apps.genre.models import Genre

from .models import MixtapeUser, set_station
from .functions import test_dic_gen_taste, station_taste

@csrf_exempt
def creat_mixtape_user(request):
    """
    pfirst_name : string which contain the first name of the user
    plast_name : string which contain the laste name of the user
    page : int which contain the age of the user
    pliked_artiste_list : list of string which containe the name of the liked artiste
    pliked_genre_list : list of string which containe the name of the liked genre
    punliked_genre_list : list of string which containe the name of the unliked genre
    lat : int which contain the latitude of the user
    longi : int which contain the longitude of the user
    """
    # pfirst_name, plast_name, page, pliked_artiste_list, pliked_genre_list,
    #  punliked_genre_list, lat, longi):
    response = {}
    if request.method == "POST" and len(request.body) > 0:
        
        postjson = json.loads(request.body.decode("utf-8"))
        if MixtapeUser.objects.get(username=postjson["user_name"]):
            response["error"] = 50
            response["errcom"] = "username allready used"
            return JsonResponse(response)

        mixtape_user = MixtapeUser(username=postjson["user_name"],
                                   first_name=postjson["first_name"],
                                   last_name=postjson["last_name"],
                                   is_facebook_user=postjson["is_facebook_user"],
                                   fb_id=postjson["fb_id"],
                                   profil_picture_url=postjson["profil_picture_url"],device=postjson["device"],
                                   gender=postjson["gender"], token=postjson["token"], age=postjson["age"],
                                   latitude=postjson["latitude"], longitude=postjson["longitude"])
        mixtape_user.save()
        try:
            pliked_artiste_list = postjson["pliked_artiste_list"]
            for liked_artiste in pliked_artiste_list:
                artiste = Artiste.objects.get(nom=liked_artiste)
                taste = Taste(points=100, genre=Genre.objects.get(nom="NULL"), artiste=artiste,
                              mixtapeUser=mixtape_user)
                taste.save()

            pliked_genre_list = postjson["pliked_genre_list"]
            for liked_genre in pliked_genre_list:
                genre = Genre.objects.get(nom=liked_genre)
                taste = Taste(points=200, genre=genre, artiste=Artiste.objects.get(nom="NULL"),
                              mixtapeUser=mixtape_user)
                taste.save()
            
            punliked_genre_list = postjson["punliked_genre_list"]
            for unliked_genre in punliked_genre_list:
                genre = Genre.objects.get(nom=unliked_genre)
                taste = Taste(points=-200, genre=genre, artiste=Artiste.objects.get(nom="NULL"),
                              mixtapeUser=mixtape_user)
                taste.save()
                response["reponse"] = "user creat with success"
        except Exception:
            response["error"] = 404

    else :
        return HttpResponseForbidden()

    return JsonResponse(response)
   
    

    
    

# def test_creat_MTuser(request):
#     """ Exemple de page HTML, non valide pour que l'exemple soit concis """
#     # code pour tester créer perso
# {
#    "is_facebook_user" : "False",
#    "fb_id" : "000",
#    "profil_picture_url" : "url",
#    "device" : "phone",
#    "gender" : "gender",
#    "token" : "token",
#    "age" : "age",
#    "latitude" : 1.0,
#    "longitude" : 1.0,
#    "pliked_artiste_list" : [ "aa", "bb", "cc"],
#    "pliked_genre_list" : ["g1", "g2", "g3", ],
#    "pliked_genre_list" : ["g4", "g5"]
# }
#     creat_mixtape_user("FN2", "LN2", 21, ["aa", "bb", "cc"], ["g1", "g2", "g3"], ["g4", "g5"], 1, 1)
#     text = """<h1>Test creat user have been executed, check out if the user had been
#      corectly created</h1>"""
#     return HttpResponse(text)

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

