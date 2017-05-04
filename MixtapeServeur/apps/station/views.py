import json

from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.shortcuts import render
from .functions import  next_song, neighbor_stations

from django.views.decorators.csrf import csrf_exempt

from .functions import next_song


from .models import Station

@csrf_exempt
def view_next_song(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    # code pour tester créer 
    
    response = {}
    if request.method == "POST" and len(request.body) > 0:
        print("view next song")
        postjson = json.loads(request.body.decode("utf-8"))
        identif = postjson["raspberryId"]
        
        try:
            print("station")
            station = Station.objects.get(mac_address=identif)
            print("bientot next song!!!!!")
            print(station.id)
            n_sg = next_song(station_id=station.id)
            print("recup next song ")
            print(n_sg)
            print(n_sg.music_uri)
            station.curent_song = n_sg.music_uri
            station.save()
            response["next_song_name"] = n_sg.nom
            response["next_song_uri"] = n_sg.music_uri  
        except Exception:
            response["error"] = 404

    else :
        return HttpResponseForbidden()

    return JsonResponse(response)

@csrf_exempt
def view_curent_song(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    # code pour tester créer 
    
    response = {}
    if request.method == "POST" and len(request.body) > 0:
        print("view next song")
        postjson = json.loads(request.body.decode("utf-8"))
        identif = postjson["raspberryId"]
        
        try:
            station = Station.objects.get(mac_address=identif)
            response["curent_song"] = station.curent_song 
        except Exception:
            response["error"] = 404

    else :
        return HttpResponseForbidden()

    return JsonResponse(response)

@csrf_exempt
def exist(request):
    """ test si la raspberry existe dans la table de donnée """
    response = {}
    if request.method == "POST" and len(request.body) > 0:

        postjson = json.loads(request.body.decode("utf-8"))
        identif = postjson["raspberryId"]
        try:
            Station.objects.get(mac_address=identif)
            response["response"] = 1    
        except Exception:
            response["response"] = 0

    else :
        return HttpResponseForbidden()

    return JsonResponse(response)

@csrf_exempt
def view_neighbor_stations(request):
    """ retourne toute les station à une 50 ène de metres """
    # code pour tester créer 
    response = {}
    print("CC")
    if request.method == "POST" and len(request.body) > 0:
        print("CC")
        postjson = json.loads(request.body.decode("utf-8"))
        stations = neighbor_stations(lat=postjson["latitude"],
                                     longi=postjson["longitude"])
        if len(stations) > 0:
            response["station_around"] = True 
            response["list"] = []
            for station in stations:
                response["list"].insert(1,{"station_name" : station.nom,
                                           "station_id" : station.id})
        else :
            response["station_around"] = False
    else :
        return HttpResponseForbidden()

    return JsonResponse(response)



