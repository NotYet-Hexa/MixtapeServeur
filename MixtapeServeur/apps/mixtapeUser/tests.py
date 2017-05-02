from django.test import TestCase
from .functions import general_taste


class general_taste_test(TestCase):
    fixtures = ['test.json',]
    
    def test_general_taste_1(self):
        """
        Vérifie si la méthode est_recent d'un Article ne
        renvoie pas True si l'Article a sa date de publication
        dans le futur.
        """
        mixtape_user_general_taste = general_taste(mixtape_user_id=9)
        correct = 1
        print(mixtape_user_general_taste)
        if mixtape_user_general_taste["g1"] != 50:
            correct *= 0
        if mixtape_user_general_taste["g2"] != 50:
            correct *= 0

        self.assertEqual(correct, 1)