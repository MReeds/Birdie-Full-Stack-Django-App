import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..connection import Connection
from BirdieApp.models import Message, model_factory

def get_messages(current_user_id, user_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Message)
        db_cursor = conn.cursor()
        
        db_cursor.execute("""
        SELECT 
            m.id,
            m.content,
            m.creator_id,
            m.recipient_id,
            u.id AS "current_user_id",
            u.username AS "current_username",
            v.id,
            v.username
        FROM BirdieApp_message m
        JOIN auth_user u, auth_user v ON m.creator_id = u.id AND m.recipient_id = v.id
        OR m.creator_id = v.id
        AND m.recipient_id = u.id
        WHERE u.id = ?
        AND v.id = ?
        ORDER BY m.id;
        """, (current_user_id, user_id))

        return db_cursor.fetchall()

@login_required
def message_details(request, user_id):
    if request.method == 'GET':
        current_user_id = request.user.id
        messages = get_messages(current_user_id, user_id)
        
        template = 'messages/details.html'
        context = {
            'user': user_id,
            'user_messages': messages
        }
        
        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        
        with sqlite3.connect(Connection.db_path) as conn:
            db_cursor = conn.cursor()
            current_user_id = request.user.id
            
            db_cursor.execute("""
            INSERT INTO BirdieApp_message
                (creator_id,
                recipient_id,
                content,
                created_at,
                expiration_date)
            VALUES
                (?, ?, ?, ?, ?);
            """,
            (current_user_id, user_id, form_data['content'], form_data['created_at'], form_data['expiration_date'],))
            
        return redirect(reverse('BirdieApp:messages'))