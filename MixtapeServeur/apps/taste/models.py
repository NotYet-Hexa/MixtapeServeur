from django.db import models
from MixtapeServeur.apps.genre.models import Genre
from MixtapeServeur.apps.artiste.models import Artiste


class Taste(models.Model):
    points = models.IntegerField()
    genre = models.ForeignKey(Genre)    
    artiste = models.ForeignKey(Artiste)
    mixtapeUser = models.ForeignKey("mixtapeUser.MixtapeUser")


    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """

        genre_name = self.genre.nom
        artiste_name  = self.artiste.nom
        #  Genre.objects.get(pk=self.genre).nom
        if genre_name == "NULL" :
            return "A-"+artiste_name+" : "+str(self.points)
        else :
            return "G-"+genre_name+" : "+str(self.points)





