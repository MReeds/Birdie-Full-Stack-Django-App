from django.urls import path
from .views import * 

app_name = 'BirdieApp'

urlpatterns = [
    path('', home, name='home'),
    path('parks/', park_list, name="parks"),
    path('park/form/', park_form, name="park_form"),
    path('bags/', bag_list, name="bags"),
    path('bag/form/', bag_form, name='bag_form'),
    path('bags/<int:bag_id>/', bag_details, name="bag"),
    path('discs/', disc_list, name="discs"),
    path('disc/form/', disc_form, name='disc_form'),
    path('discs/<int:disc_id>/', disc_details, name='disc'),
    path('discs/<int:disc_id>/form/', disc_edit_form, name="disc_edit_form"),
]