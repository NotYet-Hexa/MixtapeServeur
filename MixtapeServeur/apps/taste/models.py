from django.db import models
from MixtapeServeur.apps.genre.models import Genre
from MixtapeServeur.apps.artiste.models import Artiste


class Taste(models.Model):
    points = models.IntegerField()
    genre = models.ForeignKey(Genre, null=True, blank=True)    
    artiste = models.ForeignKey(Artiste, null=True, blank=True)
    mixtapeUser = models.ForeignKey("mixtapeUser.MixtapeUser", null=True, blank=True)


    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """

        genre_name = self.genre.nom
        artiste_name  = self.artiste.nom
        #  Genre.objects.get(pk=self.genre).nom
        if genre_name :
            return "A-"+artiste_name+" : "+str(self.points)
        else:
            if artiste_name :
                return "G-"+genre_name+" : "+str(self.points)
            else:
                return "NULL"





