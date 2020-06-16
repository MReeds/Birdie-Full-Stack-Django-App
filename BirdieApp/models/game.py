from django.db import models
from django.urls import reverse
from .park import Park
from .bag import Bag

class Game(models.Model):
    park = models.ForeignKey(Park, on_delete=models.PROTECT)
    bag = models.ForeignKey(Bag, on_delete=models.PROTECT)
    score = models.IntegerField(null=True)
    started_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = ("game")
        verbose_name_plural = ("games")
        
    def __str__(self):
        return f"This game was started at {self.started_at}. It was played at {self.park_id.title}. Final score was {self.score}."