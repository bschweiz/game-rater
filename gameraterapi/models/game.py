from django.db import models
from .rater import Rater

class Game(models.Model):

    rater = models.ForeignKey("Rater", on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=333)
    designer = models.CharField(max_length=75)
    year = models.IntegerField()
    player_count = models.IntegerField()
    duration = models.IntegerField()
    age = models.IntegerField()
    