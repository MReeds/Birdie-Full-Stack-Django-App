from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Message(models.Model):
    creator_id = models.ForeignKey(User, on_delete=models.SET_NULL)
    recipient_id = models.ForeignKey(User, on_delete=models.SET_NULL)
    content = models.CharField(null=False)
    created_at = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField()
    
    class Meta:
        verbose_name = ("message")
        verbose_name_plural = ("messages")
        
    def __str__(self):
        return self.content