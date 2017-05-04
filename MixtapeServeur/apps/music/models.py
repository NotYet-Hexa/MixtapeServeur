from django.db import models
from MixtapeServeur.apps.artiste.models import Artiste
from MixtapeServeur.apps.mixtapeUser.models import MixtapeUser

class Music(models.Model):
    nom = models.CharField(max_length=100)
    artiste = models.CharField(max_length=100)
    music_uri = models.CharField(max_length=400, default="NULL")
    mixtapeUser = models.ForeignKey(MixtapeUser)



    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.nom



