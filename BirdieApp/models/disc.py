from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext

class Disc(models.Model):
    
    class Disc_Type(models.TextChoices):
        DRIVER =  gettext('Driver')
        MIDRANGE = gettext('Mid-Range')
        PUTTER = gettext('Putter')
        
    disc_type = models.CharField(choices=Disc_Type.choices, null=False, max_length=20)
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