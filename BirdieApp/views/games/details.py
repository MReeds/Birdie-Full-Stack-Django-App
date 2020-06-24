import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from BirdieApp.models.model_factory import model_factory
from BirdieApp.models import Game


def get_game(game_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Game)
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT
            g.id AS game_id,
            g.score,
            g.started_at,
            g.user_id,
            b.brand,
            p.title
        FROM BirdieApp_game g
        JOIN BirdieApp_bag b ON b.id = g.bag_id
        JOIN BirdieApp_park p ON p.id = g.park_id
        WHERE game_id = ?
        """, (game_id,))
        
        return db_cursor.fetchone()

@login_required
def game_details(request, game_id):
    if request.method == 'GET':
        game = get_game(game_id)
        current_user = request.user.id
        
        template = 'games/details.html'
        context = {
            'game': game,
            'current_user': current_user
        }
        
        return render(request, template, context)
    
    if request.method == 'POST':
        form_data = request.POST

        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM BirdieApp_game
                WHERE id = ?
                """, (game_id,))

            return redirect(reverse('BirdieApp:games'))
        
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE BirdieApp_game
                SET game_id = ?,
                    score = ?,
                    bag_id = ?,
                    park_id = ?,
                WHERE id = ?
                """,
                (
                    form_data['game_id'], form_data['score'],
                    form_data['bag_id'], form_data['park_id'], game_id,
                ))

            return redirect(reverse('BirdieApp:games'))
