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
        AND v.id = ?;
        """, (current_user_id, user_id))

        return db_cursor.fetchall()

@login_required
def message_details(request, user_id):
    if request.method == 'GET':
        current_user_id = request.user.id
        messages = get_messages(current_user_id, user_id)
        
        template = 'messages/details.html'
        context = {
            'user_messages': messages
        }
        
        return render(request, template, context)