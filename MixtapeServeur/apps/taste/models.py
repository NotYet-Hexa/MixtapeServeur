from django.db import models
from MixtapeServeur.apps.genre.models import Genre
from MixtapeServeur.apps.artiste.models import Artiste


class Taste(models.Model):
    points = models.IntegerField()
    genre = models.ForeignKey(Genre, null=True, blank=True)
    mixtapeUser = models.ForeignKey("mixtapeUser.MixtapeUser", null=True, blank=True)


    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """

        return str(self.mixtapeUser.id)+"G-"+self.genre.nom+" : "+str(self.points)





