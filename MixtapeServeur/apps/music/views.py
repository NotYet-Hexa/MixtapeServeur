import json

from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from MixtapeServeur.apps.mixtapeUser.models import MixtapeUser
from MixtapeServeur.apps.artiste.models import Artiste
from .models import add_music_suggestion

@csrf_exempt
def view_add_music_suggestion(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    # code pour tester créer 
    
    response = {}
    if request.method == "POST" and len(request.body) > 0:

        postjson = json.loads(request.body.decode("utf-8"))        
        try:
            mixtapeUser = MixtapeUser.objects.get(pk=postjson["mixtape_user_id"])
            artiste = Artiste.objects.get(pk=postjson["artiste_id"])
            add_music_suggestion(mixtapeUser.id, postjson["music_name"], artiste.id)
            response["com"] = "suggestion added with success" 
        except Exception:
            response["error"] = 404
    else :
        return HttpResponseForbidden()

    return JsonResponse(response)

