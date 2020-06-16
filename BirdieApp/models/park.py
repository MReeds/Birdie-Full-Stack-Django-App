from django.db import models
from django.urls import reverse

class Park(models.model):
    title = models.CharField(max_length=60)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=15)

    class Meta:
        verbose_name = ("park")
        verbose_name_plural = ("parks")
        
    def __str__(self):
        return f"{self.title}, {self.city}, {self.state}"