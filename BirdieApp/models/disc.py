from django.db import models
from django.urls import reverse
from .disc_type import Disc_Type
from django.contrib.auth.models import User
from django.utils.translation import gettext

class Disc(models.Model):
        
    disc_type = models.ForeignKey(Disc_Type, null=False, on_delete=models.DO_NOTHING)
    color = models.CharField(max_length=20, null=True)
    speed = models.IntegerField(null=True)
    glide = models.IntegerField(null=True)
    turn = models.IntegerField(null=True)
    fade = models.IntegerField(null=True) 

    class Meta:
        verbose_name = ("disc")
        verbose_name_plural = ("discs")
        
    def __str__(self):
        return self.disc_type