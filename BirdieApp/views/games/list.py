import sqlite3
from django.shortcuts import render, redirect, reverse
from BirdieApp.models import model_factory, Game, Bag, Park
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def game_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(Game)
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
                SELECT
                    g.user_id,
                    g.id,
                    g.score,
                    g.started_at,
                    b.brand,
                    p.title
                FROM BirdieApp_game g
                JOIN BirdieApp_bag b ON b.id = g.bag_id
                JOIN BirdieApp_park p ON p.id = g.park_id
                ORDER BY g.started_at;
                """)
            
            all_games = db_cursor.fetchall()
        
        template = ('games/list.html')
        context = {
            'all_games': all_games,
        }
        
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        user_id = request.user.id
        
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            INSERT INTO BirdieApp_game
                (user_id, started_at, score, bag_id, park_id)
            VALUES
                (?, ?, ?, ?, ?)
            """,
            (user_id, form_data['started_at'], form_data['score'], form_data['bag_id'], form_data['park_id']))
            
        return redirect(reverse('BirdieApp:games'))
