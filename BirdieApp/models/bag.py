from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .disc_type import Disc_Type


class Bag(models.Model):
    disc = models.ForeignKey(Disc_Type, on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name = ('bag')
        verbose_name_plural = ('bags')