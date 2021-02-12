from django.db import models
from .game import Game
from .category import Category


class GameCategory(models.Model):

    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    content = models.CharField(max_length=333)