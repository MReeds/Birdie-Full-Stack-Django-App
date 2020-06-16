from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .disc import Disc


class Bag(models.Model):
    disc = models.ForeignKey(Disc, on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = ('bag')
        verbose_name_plural = ('bags')