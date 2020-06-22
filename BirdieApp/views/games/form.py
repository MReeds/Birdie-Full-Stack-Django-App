import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from BirdieApp.models import Bag, Park, model_factory
from ..connection import Connection

def get_parks():
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Park)
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            p.id AS park_id,
            p.title,
            p.city,
            p.state
        FROM BirdieApp_park p
        """)

        return db_cursor.fetchall()

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
def game_form(request):
    if request.method == 'GET':
        parks = get_parks
        bags = get_bags
        template = 'games/form.html'
        context = {
            'all_parks': parks,
            'all_bags': bags
        }

        return render(request, template, context)
