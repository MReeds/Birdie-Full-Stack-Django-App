from django.urls import path
from .views import * 

app_name = 'BirdieApp'

urlpatterns = [
    path('', home, name='home'),
    path('parks/', park_list, name="parks"),
    path('park/form', park_form, name="park_form"),
    path('bags/', bag_list, name="bags"),
    path('bags/<int:bag_id>', bag_details, name="bag"),
]