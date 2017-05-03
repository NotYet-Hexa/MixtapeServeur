from django.db import models

class Station(models.Model):
    nom = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    
    mac_address = models.CharField(max_length=17, null=True, blank=True)
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard et dans l'administration
        """
        return self.nom

