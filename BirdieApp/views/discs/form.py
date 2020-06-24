import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .details import get_disc
from ..connection import Connection
from BirdieApp.models import Bag, model_factory


types = [
    'Putter',
    'Mid-range',
    'Driver'
]

def get_bags():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Bag)
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            b.id AS bag_id,
            b.user_id,
            b.brand
        FROM BirdieApp_bag b
        """)
        
        return db_cursor.fetchall()
        
@login_required
def disc_form(request):
    if request.method == 'GET':
        template = 'discs/form.html'
        context = {
            'types': types
        }

        return render(request, template, context)
    
@login_required
def disc_edit_form(request, disc_id):

    if request.method == 'GET':
        disc = get_disc(disc_id)
        bags = get_bags

        template = 'discs/form.html'
        context = {
            'disc': disc,
            'types': types,
            'all_bags': bags
        }

        return render(request, template, context)


