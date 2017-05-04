import json

from django.http import HttpResponse, JsonResponse, HttpResponseForbidden
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from MixtapeServeur.apps.mixtapeUser.models import MixtapeUser
from MixtapeServeur.apps.artiste.models import Artiste
from .models import Music

@csrf_exempt
def view_add_music_suggestion(request):
    print("music sugg")
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    # code pour tester créer 
    
    response = {}
    if request.method == "POST" and len(request.body) > 0:

        postjson = json.loads(request.body.decode("utf-8"))        
        try:
            print("avant : ")
            print(postjson["mixtape_user_id"])
            mixtapeUser = MixtapeUser.objects.get(username=postjson["mixtape_user_id"])
            print("apres : ")
            music = Music(nom=postjson["music_name"], artiste= postjson["artiste_name"],
                           mixtapeUser=mixtapeUser, music_uri = postjson["music_uri"])
            print(music)
            music.save()
            
            response["com"] = "success" 
        except Exception as E:
            print(E)
            response["error"] = 404
    else :
        return HttpResponseForbidden()

    return JsonResponse(response)

