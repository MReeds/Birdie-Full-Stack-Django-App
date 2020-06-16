from django.urls import path
from .views import * 

app_name = 'BirdieApp'

urlpatterns = [
    path('', home, name='home'),
]