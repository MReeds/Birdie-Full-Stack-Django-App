from django.urls import path
from .views import * 

app_name = 'BirdieApp'

urlpatterns = [
    path('', home, name='home'),
    path('account/', account_details, name="account"),
    path('account/form/', account_edit_form, name="account_edit_form"),
    path('games/', game_list, name='games'),
    path('games/<int:game_id>/', game_details, name='game'),
    path('game/form/', game_form, name='game_form'),
    path('game/<int:game_id>/form/', game_edit_form, name='game_edit_form'),
    path('parks/', park_list, name="parks"),
    path('park/form/', park_form, name="park_form"),
    path('parks/<int:park_id>/', park_details, name="park"),
    path('parks/<int:park_id>/form/', park_edit_form, name="park_edit_form"),
    path('bags/', bag_list, name="bags"),
    path('bag/form/', bag_form, name='bag_form'),
    path('bags/<int:bag_id>/', bag_details, name="bag"),
    path('discs/', disc_list, name="discs"),
    path('disc/form/', disc_form, name='disc_form'),
    path('discs/<int:disc_id>/', disc_details, name='disc'),
    path('discs/<int:disc_id>/form/', disc_edit_form, name="disc_edit_form"),
    path('messages/', user_list, name="messages"),
    path('messages/<int:user_id>/', message_details, name='message'),
]