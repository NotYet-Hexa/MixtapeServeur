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


@csrf_exempt
def creat_mixtape_user(request):
    """
    pfirst_name : string which contain the first name of the user
    plast_name : string which contain the laste name of the user
    page : int which contain the age of the user
    pliked_artiste_list : list of string which containe the name of the liked artiste
    pliked_genre_list : list of string which containe the name of the liked genre
    punliked_genre_list : list of string which containe the name of the unliked genre
    """
    # pfirst_name, plast_name, page, pliked_artiste_list, pliked_genre_list,
    #  punliked_genre_list, lat, longi):
    response = {}
    if request.method == "POST" and len(request.body) > 0:
        
        postjson = json.loads(request.body.decode("utf-8"))
        if MixtapeUser.objects.filter(username=postjson["Id"]).count() > 0:
            response["error"] = 50
            response["errcom"] = "username allready used"
            return JsonResponse(response)


        mixtape_user = MixtapeUser(username=postjson["Id"],
                                   first_name=postjson["first_name"],
                                   last_name=postjson["last_name"],
                                   is_facebook_user=postjson["IsFbUser"],
                                   profil_picture_url=postjson["ProfilPictureURL"],device=postjson["Devices"],
                                   gender=postjson["Gender"], token=postjson["Token"], age=postjson["AgeRange"],)
        mixtape_user.save()
        try:
            pliked_genre_list = postjson["pliked_genre_list"]
            for liked_genre in pliked_genre_list:
                genre = Genre.objects.get(nom=liked_genre)
                taste = Taste(points=200, genre=genre,
                              mixtapeUser=mixtape_user)
                taste.save()
            
            punliked_genre_list = postjson["punliked_genre_list"]
            for unliked_genre in punliked_genre_list:
                genre = Genre.objects.get(nom=unliked_genre)
                taste = Taste(points=-200, genre=genre,
                              mixtapeUser=mixtape_user)
                taste.save()
            response["reponse"] = "user creat with success"
            response["user_id"] = mixtape_user.id
        except Exception:
            print("prob")
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



