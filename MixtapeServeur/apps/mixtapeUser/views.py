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
                response["user_id"] = mixtape_user.id
        except Exception:
            response["error"] = 404

    else :
        return HttpResponseForbidden()

    return JsonResponse(response)



@csrf_exempt
def view_set_station(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    # code pour tester set station
    print("CC")
    response = {}
    if request.method == "POST" and len(request.body) > 0:
        
        postjson = json.loads(request.body.decode("utf-8"))
        try:
            mixtape_user = MixtapeUser.objects.get(pk=postjson["mixtape_user_id"])
            station = Station.objects.get(pk=postjson["station_id"])
            set_station(mixtape_user.id, station.id)
            response["comment"]= "sation set with success"
        except Exception:
            response["error"] = 404
            response["errcom"] = "station id or mixtape user id invalid"
    else :
        return HttpResponseForbidden()
        
    return JsonResponse(response)

        
    text = """<h1>Test set station have been executed, check out if the user had been
     corectly created</h1>"""
    return HttpResponse(text)

# def test_test_gen_taste(request):
#     """ Exemple de page HTML, non valide pour que l'exemple soit concis """
#     # code pour tester créer 
#     station_taste(station_id=6)
#     text = """ <h1> Test </h1>"""
#     return HttpResponse(text)

