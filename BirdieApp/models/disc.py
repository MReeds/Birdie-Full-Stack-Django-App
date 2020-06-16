from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext

class Disc(models.Model):
    
    class Disc_Type(models.TextChoices):
        DRIVER =  gettext('Driver')
        MID-RANGE = gettext('Mid-Range')
        PUTTER = gettext('Putter')
        
    disc_type = models.CharField(choices=Disc_Type.choices)
    color = models.CharField(max_length=20)
    speed = models.IntegerField()
    glide = models.IntegerField()
    turn = models.IntegerField()
    fade = models.IntegerField() 

    class Meta:
        verbose_name = ("disc")
        verbose_name_plural = ("discs")
        
    def __str__(self):
        return self.disc_type