from django.db import models
from MixtapeServeur.apps.artiste.models import Artiste
from MixtapeServeur.apps.mixtapeUser.models import MixtapeUser

class Music(models.Model):
    nom = models.CharField(max_length=100)
    artiste = models.ForeignKey(Artiste)
    mixtapeUser = models.ForeignKey(MixtapeUser)



    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.nom

def add_music_suggestion(mixtapeUser_id, music_name, music_artiste_id):
    """
    docstring
    """
    music = Music(nom=music_name, artiste= Artiste.objects.get(pk=music_artiste_id),
                  mixtapeUser=MixtapeUser.objects.get(pk=mixtapeUser_id)) 
    music.save()

