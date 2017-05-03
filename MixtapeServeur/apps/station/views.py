import json

from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt

from .functions import next_song


from .models import Station

@csrf_exempt
def view_next_song(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    # code pour tester créer 
    
    response = {}
    if request.method == "POST" and len(request.body) > 0:

        postjson = json.loads(request.body.decode("utf-8"))
        identif = postjson["raspberryId"]
        
        try:
            Station.objects.get(mac_address=identif)
            n_sg = next_song(station_id=identif)
            response["response"] = n_sg  
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

