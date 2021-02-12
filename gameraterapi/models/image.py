from django.db import models
from .rater import Rater
from .game import Game

class Image(models.Model):

    rater = models.ForeignKey("Rater", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="games", height_field=None,
                                width_field=None, max_length=None)
    
    