from django.db import models
from django.urls import reverse

class Disc_Type(models.Model):
    name = models.CharField(null=False, max_length=15)