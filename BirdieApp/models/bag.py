from django.db import models
from django.urls import reverse

class Bag(models.Model):
    brand = models.CharField(null=True, max_length=25)
    
    class Meta:
        verbose_name = ('bag')
        verbose_name_plural = ('bags')