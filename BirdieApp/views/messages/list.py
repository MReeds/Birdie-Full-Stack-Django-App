import sqlite3
from django.shortcuts import render, redirect, reverse
from BirdieApp.models import model_factory, Message
from django.contrib.auth.models import User 
from ..connection import Connection
from django.contrib.auth.decorators import login_required

@login_required
def user_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = model_factory(User)
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
            SELECT
                id AS user_id,
                username
            FROM auth_user
            """)
            
            all_users = db_cursor.fetchall()
            
        template = ('messages/list.html')
        context = {
            'all_users': all_users
        }
        
        return render(request, template, context)

    
    # elif request.method == 'POST':
    #     form_data = request.POST
    #     user_id = request.user.id
        
    #     with sqlite3.connect(Connection.db_path) as conn:
    #         db_cursor = conn.cursor()
            
    #         db_cursor.execute("""
    #         INSERT INTO BirdieApp_game
    #             (user_id, started_at, score, bag_id, park_id)
    #         VALUES
    #             (?, ?, ?, ?, ?)
    #         """,
    #         (user_id, form_data['started_at'], form_data['score'], form_data['bag_id'], form_data['park_id']))
            
    #     return redirect(reverse('BirdieApp:games'))
